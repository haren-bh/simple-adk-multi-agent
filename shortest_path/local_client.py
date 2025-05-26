import vertexai
from agent import root_agent

PROJECT_ID = "datapipeline-372305"
LOCATION = "us-central1"
STAGING_BUCKET = "gs://haren-genai-data"

vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
    staging_bucket=STAGING_BUCKET,
)

from vertexai.preview import reasoning_engines

app = reasoning_engines.AdkApp(
    agent=root_agent,
    enable_tracing=True,
)
session = app.create_session(user_id="u_123")
print(session)
for event in app.stream_query(
    user_id="u_123",
    session_id=session.id,
    message="Find the shortest route between Tokyo, London and Paris.",
):
    print(event)


