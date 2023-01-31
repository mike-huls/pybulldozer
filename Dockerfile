# FINAL image
FROM python:3.9-slim AS final

# BUILD image
FROM python:3.9-slim AS build
WORKDIR /app/
ENV PATH="/app/venv/bin:$PATH"

# install dependencies
RUN apt-get update --no-install-recommends



# install python packages in the venv
# Make sure PYPI_PASS and PYPI_USER are in the .env and to
SHELL ["/bin/bash", "-c"]
COPY requirements.txt .
# pip install requirements WITH custom index url
RUN --mount=type=secret,id=pypi_creds source /run/secrets/pypi_creds \
    && python -m venv /app/venv \
    && python -m pip install --upgrade pip \
    && python -m pip install --extra-index-url https://${PYPI_USER}:${PYPI_PASS}@${PYPI_URL} -r requirements.txt
# pip install requirements WITHOUT custom index url
# RUN python -m venv /app/venv \
#     && python -m pip install --upgrade pip \
#     && python -m pip install -r requirements.txt


# Construct the final image
FROM final
WORKDIR /app/
ENV PATH="/app/venv/bin:$PATH"

# For SQL SERVER DRIVER
# ENV ACCEPT_EULA=Y
# RUN apt-get update -y && apt-get update \
#   && apt-get install -y --no-install-recommends curl gcc g++ gnupg unixodbc-dev
# RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
#     && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
#     && apt-get update \
#     && ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Copy the entire venv from the build layer
COPY --from=build /app/venv /app/venv

# copy source code
COPY ./ .


ENTRYPOINT ["uvicorn"]
CMD ["main:app", "--host", "0.0.0.0"]
# ENTRYPOINT ["/bin/bash"]