FROM golang:1.23 AS builder

WORKDIR /app

# copy source code. go.mod, go.sum 포함
COPY . .
# C 빌드 바이너라 파일 포함
RUN go mod download \
&& CGO_ENABLED=0 go build -o mocking-server

# stage 2 build
FROM alpine:latest

WORKDIR /home

COPY --from=builder /app/mocking-server .

EXPOSE 9000

ENTRYPOINT [ "./mocking-server" ]
