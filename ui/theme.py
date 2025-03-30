# Color scheme variables
dark_background = "#111827"
light_background = "#1f2937"
lighter_background = "#374151"
button_blue = "#4C82FB"
button_green = "#007b86"
purple_accent = "#9D5CF7"
card_bg = "#374151"
text_color = "#FFFFFF"
muted_text = "#A0A0A0"
icon_blue = "#4C82FB"

# UI Constants
BLUE_CIRCLE_ICON = '<span style="display: inline-block; width: 18px; height: 18px; border: 5px solid #007b86; border-radius: 50%; vertical-align: middle; margin-right: 5px;"></span>'

# CSS Styling
css = f"""
.gradio-container {{background-color: {dark_background} !important;}}
.main-panel {{padding-right: 15px; margin-right: 15px; background-color: {dark_background}; }}
.left-panel {{background-color: {light_background}; border-radius: 10px; padding: 10px; margin: 15px;}}
.example-questions {{background-color: {light_background}; border-radius: 10px; padding: 15px; margin-bottom: 20px; }}
.full-width-header {{background-color: {light_background}; padding: 15px; width: 100%; display: flex; justify-content: space-between; align-items: center;}}
.header {{
display: flex;
font-size: 24px;
font-weight: bold;
}}
.header-settings {{
    align-items: center;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
    padding-right: 100px;
}}
.header-text {{
    background-image: linear-gradient(to right, #007b86, #ffffff);
    background-size: 100%;
    background-clip: text;
    -webkit-background-clip: text;
    -moz-background-clip: text;
    -webkit-text-fill-color: transparent; 
    -moz-text-fill-color: transparent;
    display: inline-block; 
}}
.header-icons {{display: flex; align-items: center;}}
.chat-icon {{color: {button_blue}; margin-right: 10px;}}
.settings-icon {{color: {text_color}; font-size: 24px; cursor: pointer; transition: color 0.3s;}}
.settings-icon:hover {{color: {button_blue};}}
.section-title {{color: {text_color}; background-color: {dark_background}; padding: 10px; margin: 10px; font-size: 20px; margin-bottom: 15px;}}             
.history-item {{padding: 8px 0; color: {text_color};}}
.question-button {{background-color: {dark_background}; color: {text_color}; text-align: left; padding: 12px; 
                    border-radius: 8px; margin-bottom: 0px; border: none;}}    
.capabilities {{background-color: {light_background}; border-radius: 10px; padding: 15px;}}
.capability-card {{background-color: {dark_background}; border-radius: 8px; padding: 10px; margin: 10px;}}              
.capability-title {{color: {text_color}; background-color: {dark_background}; font-size: 16px; font-weight: 600;}}
.capability-subtitle {{color: {muted_text}; background-color: {dark_background}; font-size: 14px;}}
.capability-group {{background-color: {dark_background}; }}
.capability-row {{padding-right: 10px;  }}
.capability-column {{  padding: 0 5px; }}
.capability-column-divider {{ padding: 0 10px }}
.clear-history-btn {{ margin-top: 10px; }}
.footer-bar {{background-color: {light_background}; padding: 10px; border-radius: 8px; margin-top: 30px; margin-bottom: 30px;}}
.send-button {{background-color: {button_green}; color: white; border-radius: 8px; margin-top: 10px; font-weight: 200;}}
.back-button {{background-color: {button_green}; color: white; border-radius: 8px; padding: 6px 12px; margin-bottom: 20px; max-width: 30px;}}
.settings-panel {{background-color: {card_bg}; border-radius: 10px; padding: 20px; margin: 15px;}}
.settings-container {{background-color: {dark_background}; padding: 20px;}}
.settings-btn {{background: none; border: none; color: {text_color}; font-size: 24px; width: 70px; align-self: flex-end; 
                cursor: pointer; transition: color 0.3s; padding: 0; margin: 0;}}
.settings-btn:hover {{color: {button_blue};}}
.response-box {{ padding-bottom: 30px; }}
"""

# JavaScript for chat history functionality
js_head = """
<script>
    // Function to update chat history that will be called when needed
    function populateChatHistory() {
        // Try to get questions from localStorage
        let questions = [];
        try {
            const storedQuestions = localStorage.getItem('userQuestions');
            if (storedQuestions) {
                questions = JSON.parse(storedQuestions);
            }
        } catch (e) {
            console.error('Error loading questions from localStorage:', e);
        }
        
        // Find the history container
        const historyContainer = document.getElementById('chat-history-items');
        if (!historyContainer) {
            console.error('Chat history container not found');
            // If container not found, retry after a short delay
            setTimeout(populateChatHistory, 100);
            return;
        }
        
        // Generate HTML for the questions
        let historyHTML = '';
        if (!questions || questions.length === 0) {
            historyHTML = '<div class="history-item">No previous questions</div>';
        } else {
            // Get the most recent questions first
            const recentQuestions = questions.slice(-10).reverse();
            
            for (const question of recentQuestions) {
                // Escape HTML to prevent XSS
                const escapedQuestion = String(question)
                    .replace(/&/g, '&amp;')
                    .replace(/</g, '&lt;')
                    .replace(/>/g, '&gt;')
                    .replace(/"/g, '&quot;')
                    .replace(/'/g, '&#039;');
                
                historyHTML += `<div class="history-item">${escapedQuestion}</div>`;
            }
        }
        
        // Update the container
        historyContainer.innerHTML = historyHTML;
    }
    
    // Make populateChatHistory available globally
    window.populateChatHistory = populateChatHistory;
       
    //  DOM content loaded event
    document.addEventListener('DOMContentLoaded', function() {
        setTimeout(populateChatHistory, 200);
        
        // Add submit event listener to populate chat history after submission
        const sendButton = document.querySelector('.send-button');
        if (sendButton) {
            sendButton.addEventListener('click', function() {
                setTimeout(populateChatHistory, 500);
            });
        }
    });
    
    // Window load event (happens after all resources are loaded)
    window.addEventListener('load', function() {
        setTimeout(populateChatHistory, 300);
    });
    
    // Immediate execution with retry mechanism
    (function initChatHistory() {
        // Try to populate immediately
        setTimeout(populateChatHistory, 100);
        
        // And try again after a short delay
        setTimeout(populateChatHistory, 500);
        
        // And once more after a longer delay
        setTimeout(populateChatHistory, 1000);
    })();
</script>
"""