"""
Culture Quest page for DesiVerse application.
Displays an interactive quiz about Indian culture and heritage.
"""

import streamlit as st
import random
import sys
import os

# Add the project root to the path so imports work correctly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.constants import quiz_questions

def show_quiz():
    """Display an interactive quiz about Indian art and culture."""
    st.markdown("<h1 class='main-header'>🎯 Culture Quest</h1>", unsafe_allow_html=True)
    
    if 'quiz_state' not in st.session_state or st.session_state.get('quiz_reset', False):
        questions = quiz_questions.copy()
        random.shuffle(questions)
        st.session_state.quiz_state = {
            'questions': questions,
            'current_question': 0,
            'score': 0,
            'selected_option': None,
            'show_feedback': False,
            'quiz_completed': False,
            'show_balloons': False
        }
        st.session_state.quiz_reset = False
    
    state = st.session_state.quiz_state
    
    if state['quiz_completed']:
        if st.button('Restart Quiz'):
            questions = quiz_questions.copy()
            random.shuffle(questions)
            st.session_state.quiz_state = {
                'questions': questions,
                'current_question': 0,
                'score': 0,
                'selected_option': None,
                'show_feedback': False,
                'quiz_completed': False,
                'show_balloons': False
            }
            st.rerun()
        st.success(f'Quiz completed! Your score: {state["score"]}/10')
        return
    
    questions = state['questions']
    current_q = state['current_question']
    score = state['score']
    q = questions[current_q]
    st.markdown(f"**Q{current_q+1}: {q['question']}**")
    options = q['options']
    
    # Show options as buttons
    option_clicked = None
    for i, option in enumerate(options):
        if st.button(option, key=f"option_{i}_{current_q}"):
            option_clicked = option
    
    if option_clicked and not state['show_feedback']:
        state['selected_option'] = option_clicked
        state['show_feedback'] = True
        if option_clicked == q['correct']:
            state['score'] += 2
            state['show_balloons'] = True
        st.session_state.quiz_state = state
        st.rerun()
    
    if state['show_balloons']:
        st.balloons()
        state['show_balloons'] = False
        st.session_state.quiz_state = state
    
    if state['show_feedback']:
        if state['selected_option'] == q['correct']:
            st.success('Correct!')
        else:
            st.error(f'Incorrect. The correct answer is: {q["correct"]}')
        if st.button('Next Question', key=f'next{current_q}'):
            if current_q + 1 < 5:
                state['current_question'] += 1
                state['selected_option'] = None
                state['show_feedback'] = False
                st.session_state.quiz_state = state
                st.rerun()
            else:
                state['quiz_completed'] = True
                st.session_state.quiz_state = state
                st.rerun()
    
    st.info(f'Score: {state["score"]}/10')
    
    # Display quiz instructions
    st.markdown("""
    <div class='insights-card'>
        <h3>About this Quiz</h3>
        <p>Test your knowledge about Indian cultural heritage with these questions. 
        Learn interesting facts about art forms, crafts, and cultural traditions from across India.</p>
        <p>New questions are added regularly!</p>
        <p><b>Each question carries 2 marks. Total: 10 marks for 5 questions.</b></p>
    </div>
    """, unsafe_allow_html=True) 