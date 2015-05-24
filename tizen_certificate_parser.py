from xml.dom.minidom import parse
import xml.dom.minidom
import sys
import chilkat
cert = chilkat.CkCert()
print "Tizen Certificate Validator"
x=raw_input("Enter Path to author-signature.xml or signature1.xml: ")
DOMTree = xml.dom.minidom.parse(x)
collection = DOMTree.documentElement
if collection:
	print "Extracting Certificate Information From: " + x
	certs = collection.getElementsByTagName("X509Certificate")
	for c in certs:
		dat=str(c.firstChild.nodeValue)
		success = cert.LoadFromBase64(dat)
		if (success != True):
			print(cert.lastErrorText())
			sys.exit()
		print("\n\n")
		print("SubjectDN:" + cert.subjectDN())
		print("Common Name:" + cert.subjectCN())
		print("Issuer Common Name:" + cert.issuerCN())
		print("Serial Number:" + cert.serialNumber())
		print("SHA1:" + cert.sha1Thumbprint())
		print("Version: " + str(cert.get_CertVersion()))
		print("Valid from: " + cert.validFromStr() + " until: "+ cert.validToStr())
	sys.exit()
else:
	print "Error: Invalid File"
	sys.exit()
		

