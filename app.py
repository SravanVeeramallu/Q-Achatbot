import gradio as gr
from difflib import get_close_matches

# Environmental tips knowledge base
eco_responses = {
    "how to save water": "Fix leaks, turn off taps when brushing, and use water-efficient appliances.",
    "how to reduce plastic use": "Use reusable bags, bottles, and avoid single-use plastics.",
    "how to conserve electricity": "Unplug devices, use LED bulbs, and turn off lights when not needed.",
    "how to compost at home": "Use kitchen scraps, garden waste, and maintain a healthy carbon-nitrogen balance.",
    "how to reduce carbon footprint": "Use public transport, eat local, and reduce meat consumption.",
    "what is climate change": "Long-term shifts in temperature and weather patterns caused by human activities.",
    "why should we plant trees": "Trees absorb CO2, provide oxygen, and support biodiversity.",
    "what is sustainability": "Meeting our needs without compromising future generations’ ability to meet theirs.",
    "how to recycle correctly": "Sort your recyclables, clean containers, and follow your local recycling rules.",
    "bye": "Thanks for caring about the planet! 🌍💚"
}

def ecobot(user_input):
    user_input = user_input.lower().strip()
    match = get_close_matches(user_input, eco_responses.keys(), n=1, cutoff=0.5)
    if match:
        return eco_responses[match[0]]
    return "Sorry, I didn't get that. Try asking about recycling, water saving, or climate change."

iface = gr.Interface(fn=ecobot,
                     inputs=gr.Textbox(lines=2, placeholder="Ask me about the environment..."),
                     outputs="text",
                     title="🌱 EcoBot – Daily Green Guide",
                     description="Ask me anything about sustainability, green habits, or climate change!")

iface.launch()
