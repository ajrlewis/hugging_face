summarize = "Summarize the following text: `{text}`. Return only the summary of the text in your response."
extract = "Extract (infer if not present) these data points: {data_points}, from the following text: `{text}`. Return only the extracted data points as a JSON object in your response. Do not include any other text."
sentiment = "Determine the sentiment from the following text: `{text}`. Return only 'positive', 'negative' or 'neutral' depending on the sentiment."


def render(template: str, **kwargs) -> str:
    return template.format(**kwargs)
