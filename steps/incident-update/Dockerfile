FROM relaysh/core:latest-python
RUN pip install pdpyras
COPY "./step.py" "/entrypoint.py"
ENTRYPOINT []
CMD ["python3", "/entrypoint.py"]

LABEL "org.opencontainers.image.title"="Splunk On-Call Incident update"
LABEL "org.opencontainers.image.description"="This step updates an incident in Splunk On-Call"
LABEL "com.puppet.nebula.sdk.version"="v1"
