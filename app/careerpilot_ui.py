
import gradio as gr
from src.services.job_recommendation import recommend_jobs


def generate_recommendations(
    education, skills, experience, interests, location, language
):
    return recommend_jobs(
        education, skills, experience, interests, location, language
    )


with gr.Blocks(title="CareerPilot") as demo:
    gr.Markdown("# CareerPilot - AI Job Recommendation Assistant")
    gr.Markdown(
        "Enter your background and preferences to discover suitable career paths."
    )

    education = gr.Textbox(
        label="Education",
        placeholder="e.g. ICT Engineering student"
    )

    skills = gr.Textbox(
        label="Skills",
        lines=3,
        placeholder="e.g. Python, networking, HTML"
    )

    experience = gr.Textbox(
        label="Work Experience",
        lines=3,
        placeholder="e.g. Customer service"
    )

    interests = gr.Textbox(
        label="Career Interests",
        placeholder="e.g. Software development, AI"
    )

    location = gr.Textbox(
        label="Preferred Job Location",
        value="Helsinki, Finland"
    )

    language = gr.Dropdown(
        choices=["English", "Finnish", "Swedish"],
        value="English",
        label="Response Language"
    )

    recommend_button = gr.Button(
        "Find Suitable Jobs",
        variant="primary"
    )

    results = gr.Markdown(label="AI Recommendations")

    recommend_button.click(
        fn=generate_recommendations,
        inputs=[
            education,
            skills,
            experience,
            interests,
            location,
            language
        ],
        outputs=results
    )


if __name__ == "__main__":
    demo.launch()
