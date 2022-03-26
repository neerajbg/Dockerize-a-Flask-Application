FROM python:3.9-alpine

# Set working directory
WORKDIR /flask

# Copy all files across
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port in the container
EXPOSE 5000

CMD [ "python", "app.py" ]