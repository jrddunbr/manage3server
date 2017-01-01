# manage3server

manage3server is a project of mine to continue developing a server room monitoring system.

A list of items in the manage3 "suite"

- manage3server is the server daemon (collects all data and compiles it)
- manage3client is the client daemon (runs on servers to track status)
- manage3js is the javascript application to display outputs from manage3server
- manage3network is the network daemon (which will connect to SNMP switches)
- manage3sensor is the sensor daemon, which interfaces sensors
- manage3battery is the battery backup daemon, which interfaces battery backups

## Progress of manage3server (not the "suite")

- [x] UDP server communication
- [x] UDP battery communication
- [x] UDP sensor communication
- [x] UDP network communication
- [x] TCP server communication
- [ ] TCP sensor communication
- [ ] Auto-removal of old keys from database
- [x] Parse to json file for manag3js to read
- [ ] Read-only REST API
- [ ] Proper logging of errors to logfile(s)
- [ ] Unit Tests
- [ ] message encryption and signatures for sensitive data
- [ ] Install script?
- [ ] aur-style package file (for easy install from the git repo for Arch systems)
