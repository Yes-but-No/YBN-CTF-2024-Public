FROM openjdk:8u181-jdk-alpine
RUN addgroup -S ybn && adduser -S ybn -G ybn --gecos 'YBN{l0gg3rs-c4ugh+_l0gg1ng_acfbd964a73}'
RUN mkdir -p /usr/src/app
ARG JAR_FILE=target/*.jar
ENV FLAG "Flag is in GECOS."
WORKDIR /usr/src/app
COPY ${JAR_FILE} app.jar
RUN chmod ugo=r app.jar
USER ybn:ybn
ENTRYPOINT ["java","-jar","/usr/src/app/app.jar"]
