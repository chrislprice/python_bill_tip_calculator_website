# 1. Use an official, small Python runtime as a parent image
FROM python:3.11.14-alpine3.23

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy only the requirements first (optimizes Docker caching)
COPY requirements.txt .

RUN apt-get update
RUN apt-get upgrade -y
RUN pip install --no-cache-dir -r requirements.txt
RUN rm -rf /var/lib/apt/lists/*

# 4. Install dependencies
#RUN  pip install --upgrade pip \ 
 #&& pip install --no-cache-dir -r requirements.txt \
  #   && sudo apt update -y \
   #  && sudo apt upgrade -y 
# 5. Copy the rest of your application code
COPY . .

# 6. Expose the port Flask runs on
EXPOSE 8081

# 7. Run the application
CMD ["python", "Python_website_two.py"]
