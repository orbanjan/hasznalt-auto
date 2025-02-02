# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page
html = scraperwiki.scrape("https://www.hasznaltauto.hu/talalatilista/PCOHKVGLN3RTADH4C574BQTRTZKY7OZIKBQBD5GUVPA5VDFNLAJAGSJWTIKP355FFQ5WW65TXGCBQSXEOA6BJCCNFK7JYWDFEJU4AY2FK3BBDO7ETGYZKSG4BU22UK5UTZ5GQIYSKDZYHRYBV6SS3UND5OQAI52LTY7UIOQU5EMFMYDTFVGSREUKERMWNYBTIADZDLGS7DVU63CFQKW42Z7XR6HRFYL2FGZE3NR57Q4BZHXOX6IRUEZSUB6H4BVL3O7DI57K773SFKOAQIUSIKHJDYOMRAQIUDEDZSBRRUH3JKDK6T2CB7JECKTEYTT26Q7B7WZMCWRROOD3HCHTRK3T4KQVRQ6XSIDGY5OHEYNEZQJQP4AHSGULVZK54BICJR6RXBJ4FQ746T3HJ4JSFYG65KVSL4ZOJMOJUZS4X5UJ2J75LM5P6ZSJSOLWIXWLTDPPLN66L6H4HRHJHCYXILZW32I2M6URZKR72W5QFTZKEBS3OEVC7SAYFQ6E3UXQ742E7IGBG2IMWMTULKZ4NG25RCBMQVFCKJBYNR2Z5UHPXQKOLZPFU52GWXYB25X4WXAI7DXEHNMZVJP7MQT3ENVS4PH4Q5MAU76ZFPNXLHPT2X72RYXDT4MOPDP6RJONM6U6R4ZBYXKFXXRPGBL2R3UNIAU3REAPRW3GHI7IFAUVMMOOIKOMK6A54J2YYNZB33CHQG3ZWFHDLGQKNVV73EWYHQ3WGFSUMBLVFE5T672WQTM6URK6Q4EG6IIKZL2CPWR2MVZHBPXQSSY73YGA2HVGA3Q4HZG4VXQ2K2NG7AXPRBSO6JZ6MJSGKFQ6HA7XLQHB6CTGS5BA7VPSBYMLTAB55JF6QPNL2YXTFWSO3YNDFV3OTJRSLUC5CZCDWMSUSOSWVCXP4ON4LGZ4IX4R22EU2SZVDQ6LYLO5AXGR4UT3EFJIHXQ7SHKF4YO7URKFVPIUZSD674ARTC55G4")
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
