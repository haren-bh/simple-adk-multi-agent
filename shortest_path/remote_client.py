import vertexai
from agent import root_agent

PROJECT_ID = "datapipeline-372305"
LOCATION = "us-central1"
STAGING_BUCKET = "gs://haren-genai-data"

from vertexai import agent_engines

reasoning_engine_id="projects/85469421903/locations/us-central1/reasoningEngines/6344489955523297280"

#remote agents.
vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
    staging_bucket=STAGING_BUCKET,
)

# Create a session service client
remote_agent = agent_engines.get(reasoning_engine_id)
print(remote_agent)
remote_session=remote_agent.create_session(user_id="u_456")

for event in remote_agent.stream_query(
    user_id="u_456",
    session_id=remote_session["id"],
    message="Find the shortest route between Tokyo, London and Paris.",
):
    print(event)
