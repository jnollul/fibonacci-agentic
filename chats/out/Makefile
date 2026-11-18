json2md=$(HOME)/src/copilot-chat-to-markdown/chat_to_markdown.py
SRC=$(wildcard ../*.json)
TARGET=$(patsubst ../%.json,%.md,$(SRC))

all: $(TARGET)

what:
	echo $(SRC)
	echo $(TARGET)

%.md: ../%.json
	python3 $(json2md) $< $@
