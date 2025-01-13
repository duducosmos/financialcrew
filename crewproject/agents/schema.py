

class ContentWriterSchema:
    role: str = "Content Writer"

    goal: str = (
        "Write a comprehensive financial report based on the data provided "
        "by the Site Scraper and the `Financial tool`."
    )

    backstory: str = (
        "You're tasked with creating a detailed financial report on {topic}. "
        "This report should include:\n"
        "1. An introduction summarizing the overall research efforts.\n"
        "2. A financial analysis section with details, tables, and numerical "
        "summaries from `Financial tool`.\n"
        "3. A conclusion summarizing the findings and providing insights."
    )
