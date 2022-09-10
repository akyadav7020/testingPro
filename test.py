# importing module
from bs4 import BeautifulSoup

markup = markup = """

<!DOCTYPE>
<html>
<head><title>Example</title></head>
	<body>

<p>
		Nested div
	</p>

		<div id="first"> Div with ID first
		<ytd-app>
		<p> hello </p>
		<div id="second" class ="first"> Div with id second
		<p> hi </p>
		</div> </ytd-app>
		</div>
	</body>
</html>
"""

# parsering string to HTML
soup = BeautifulSoup(markup, 'html.parser')

# finding the div with the id
div_bs4 = soup.find('ytd-app')#, id="second",class ="first")

print(div_bs4)
