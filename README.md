<h1 align="center">
  <br>
  Confluence CVE_2022_26134 detect
  </h1>

<h4 align="center">Simple Python 3 script to detect the "Confluence RCE CVE_2022_26134" vulnerability (CVE_2022_26134) for a list of URL with multithreading </h4>

---

To do so, it sends a GET request using threads (higher performance) to each of the URLs in the specified list. The GET request contains a payload that on success returns a DNS request to Burp Collaborator / interactsh. Finally, if a host is vulnerable, an identification number will appear in the subdomain prefix of the Burp Collaborator / interactsh payload and in the output of the script, allowing to know which host has responded via DNS. It should be noted that this script only handles DNS detection of the vulnerability and does not test remote command execution ;).

---

### Usage


