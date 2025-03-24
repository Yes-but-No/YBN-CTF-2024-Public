FROM amazoncorretto:23-alpine
RUN addgroup -S ybn && adduser -S ybn -G ybn --gecos 'YBN{S4n1ti$3-Your-1npUt$-Pr0p3rlY-Thymeleaf-a7d4ac913d95f43}'
RUN mkdir -p /usr/src/app
USER ybn:ybn
ARG JAR_FILE=target/*.jar
ENV FLAG "Flag is in GECOS."
WORKDIR /usr/src/app
COPY ${JAR_FILE} app.jar
ENTRYPOINT ["java","-jar","/usr/src/app/app.jar"]
