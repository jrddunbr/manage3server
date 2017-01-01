all: local
cosi:
	cp cosi-conf configs -r
local:
	cp local-conf configs -r
	cp local-users users -r
clean:
	rm configs -r
	rm users -r
