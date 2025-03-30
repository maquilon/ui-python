import gradio as gr
from handlers import question, show_settings_page, show_main_page
from ui.components import create_main_app, create_settings_page
from ui.theme import css, js_head

# Main application
with gr.Blocks(theme=gr.themes.Base(), css=css, head=js_head) as demo:
    # Two pages: main app and settings
    main_app = gr.Group(visible=True)
    settings_page = gr.Group(visible=False)
    
    # Build the UI components
    with main_app:
        settings_btn, user_input, submit_btn, output, example_buttons = create_main_app()
            
    with settings_page:
        back_btn, clear_history_btn = create_settings_page()
    
    # Connect the example buttons to input field
    for example in example_buttons:
        example.click(
            fn=lambda text: text,
            inputs=[example],
            outputs=[user_input]
        )
    
    # Connect the AI to the user inputs with localStorage saving
    submit_btn.click(
        question, 
        inputs=[user_input], 
        outputs=[output],
        js="""
        function(user_question) {
            try {
                // Get existing questions from localStorage
                let questions = [];
                try {
                    const storedQuestions = localStorage.getItem('userQuestions');
                    if (storedQuestions) {
                        questions = JSON.parse(storedQuestions);
                    }
                } catch (e) {
                    console.error('Error parsing questions:', e);
                    questions = [];
                }
                
                // Add the new question
                if (user_question && user_question.trim() !== '') {
                    questions.push(user_question);
                    
                    // Save back to localStorage
                    localStorage.setItem('userQuestions', JSON.stringify(questions));
                    console.log('Saved question to localStorage:', user_question);
                    
                    // Manually call our populate function
                    setTimeout(function() {
                        if (window.populateChatHistory) {
                            window.populateChatHistory();
                        }
                    }, 100);
                }
            } catch (e) {
                console.error('Error saving to localStorage:', e);
            }
            
            return user_question;
        }
        """
    )
    
    # Set up navigation between pages
    settings_btn.click(show_settings_page, inputs=[], outputs=[settings_page, main_app])
    back_btn.click(show_main_page, inputs=[], outputs=[settings_page, main_app])
    
    # Add JS to clear localStorage when the button is clicked
    clear_history_btn.click(
        fn=lambda: None,
        inputs=[],
        outputs=[],
        js="""
        () => {
            localStorage.removeItem('userQuestions');
            alert('Chat history cleared');
            
            // Update the display
            if (window.populateChatHistory) {
                window.populateChatHistory();
            }
        }
        """
    )

# Launch the app
if __name__ == "__main__":
    demo.launch()