from agents.agent import Agent
from agents.executive import Executive


class Chairman(Agent):
    def __init__(self, name: str, executives: list):
        super().__init__(name)
        self.executives = executives

    def decide_if_meeting_over(self, minutes: list, transcript: list) -> bool:
        return False

    def decide_next_speaker(self, minutes_list: list, transcript_list: list) -> Executive:
        minutes = " ".join(minutes_list)
        transcript = " ".join(transcript_list)

        while True:
            prompt = f"Given the transcript: {transcript}, who should speak next among the following executives? answer with only the name and nothing else\n"
            for executive_agent in self.executives:
                prompt += f"{executive_agent.name}: expert in {executive_agent.expertise} and concerned about {', '.join(executive_agent.concerns)}.\n"

            next_speaker = self.query_gpt(prompt, 50).strip()

            next_executive = next((exec for exec in self.executives if exec.name == next_speaker), None)

            if next_executive is not None:
                return next_executive

            print(f"{next_speaker} is not a valid exec...")