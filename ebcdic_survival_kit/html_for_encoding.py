'''
Write HTML Table showing all characters of an 7 or 8 bit encoding.
'''
import cgi
import codecs
import logging
import os
import string

#import cp273

_log = logging.getLogger('html')

_CONTROL_CODE_NAMES = [
    'NUL',
    'SOH',
    'STX',
    'ETX',
    'EOT',
    'ENQ',
    'ACK',
    'BEL',
    'BS',
    'HT',
    'LF',
    'VT',
    'FF',
    'CR',
    'SO',
    'SI',
    'DLE',
    'DC1',
    'DC2',
    'DC3',
    'DC4',
    'NAK',
    'SYN',
    'ETB',
    'CAN',
    'EM',
    'SUB',
    'ESC',
    'FS',
    'GS',
    'RS',
    'US',
]
_UNPRINTABLE_TO_NAME_MAP = {
    '\x7f': 'DEL',
}
for code, name in enumerate(_CONTROL_CODE_NAMES):
    _UNPRINTABLE_TO_NAME_MAP[chr(code)] = name
_STYLE = u'<style style="display:none">pre.lua.source-lua{font-family:monospace,Courier}.ui-helper-clearfix:before,.ui-helper-clearfix:after{border-collapse:collapse}.Person{font-style:normal;font-variant:small-caps}p.Zitat{font-style:normal;margin-bottom:0}p.cite{margin-top:0;padding-left:1em}cite{font-style:normal}cite{font-style:inherit}div.NavFrame{display:inline-block}div.NavFrame{border:1px solid #aaa;clear:both;display:block;font-size:95%;margin-top:1.5em;padding:2px;text-align:center}div.NavPic{float:left;padding:2px}div.NavHead{background:#efefef;font-weight:bold}div.NavFrame:after{clear:both;content:"";display:block}div.NavEnd{display:none}.NavToggle{float:right;font-size:x-small}div.NavFrame + div.NavFrame{margin-top:-1px}div.BoxenVerschmelzen{border:1px solid #aaa;clear:both;font-size:95%;margin-top:1.5em;padding-top:2px}div.BoxenVerschmelzen div.NavFrame{border:none;font-size:100%;margin:0;padding-top:0}div.sideBox{background:white;border:1px solid gray;clear:right;float:right;margin-left:1em;overflow:hidden;padding:0.3em;position:relative;width:200px}div.sideBox dl{font-size:96%;margin:0 0 0.3em}div.sideBox dl dt{background:none;margin:0.4em 0 0}div.sideBox dl dd{background:#f3f3f3;margin:0.1em 0 0 1.1em}table.taxobox,table.palaeobox{background:white;border:1px solid gray;border-collapse:collapse;clear:right;float:right;margin:1em 0 1em 1em}table.taxobox th,table.palaeobox th{background:#9bcd9b;border:1px solid gray;font-weight:bold;text-align:center}table.palaeobox th{background:#e7dcc3}table.taxobox div.thumb,table.taxobox div.thumb *,table.palaeobox div.thumb,table.palaeobox div.thumb *{background:#f9f9f9;border:none;float:none;margin:0 auto;padding:0}table.taxobox div.magnify,table.palaeobox div.magnify{display:none}table.taxobox tr td div.thumb div div.thumbcaption,table.taxobox td.Person,table.taxobox td.taxo-name,table.taxobox td.taxo-bild,table.palaeobox tr td div.thumb div div.thumbcaption,table.palaeobox td.Person,table.palaeobox td.taxo-name,table.palaeobox td.taxo-bild,table.palaeobox td.taxo-zeit{text-align:center}table.palaeobox td.taxo-ort{text-align:left}.prettytable{background-color:#f9f9f9;border:1px solid #aaa;border-collapse:collapse;color:black;margin:1em 0}table.prettytable>*>tr>th,table.prettytable>*>tr>td{border:1px solid #aaa;padding:0.2em}table.prettytable>*>tr>th{text-align:center}table.prettytable>caption{font-weight:bold}table.wikitable.zebra>tbody>:nth-child(even):not([class*="hintergrundfarbe"]){background:white}div.float-left,table.float-left,ul.float-left,.float-left{clear:left;float:left;margin:1em 1em 1em 0}div.float-right,table.float-right,ul.float-right,.float-right{clear:right;float:right;margin:1em 0 1em 1em}div.centered,table.centered,ul.centered,.centered{margin-left:auto;margin-right:auto}.toptextcells>*>*>td{vertical-align:top}table ul,table p{margin-top:.3em}.metadata{display:none}.metadata-label{color:#aaa}table.metadata{border:1px solid #aaa}.rahmenfarbe1{border:1px #aaa}.rahmenfarbe2{border:1px #e9e9e9}.rahmenfarbe3{border:1px #c00000}.rahmenfarbe4{border:1px #88a}.rahmenfarbe5{border:1px #000}table>*>tr.hintergrundfarbe1>th,table>*>tr>th.hintergrundfarbe1,table.hintergrundfarbe1,.hintergrundfarbe1{background-color:#f9f9f9}table>*>tr.hintergrundfarbe2>th,table>*>tr>th.hintergrundfarbe2,table.hintergrundfarbe2,.hintergrundfarbe2{background-color:#fff}table>*>tr.hintergrundfarbe3>th,table>*>tr>th.hintergrundfarbe3,table.hintergrundfarbe3,.hintergrundfarbe3{background-color:#ffff40}table>*>tr.hintergrundfarbe4>th,table>*>tr>th.hintergrundfarbe4,table.hintergrundfarbe4,.hintergrundfarbe4{background-color:#fa0}table>*>tr.hintergrundfarbe5>th,table>*>tr>th.hintergrundfarbe5,table.hintergrundfarbe5,.hintergrundfarbe5{background-color:#e0e0e0}table>*>tr.hintergrundfarbe6>th,table>*>tr>th.hintergrundfarbe6,table.hintergrundfarbe6,.hintergrundfarbe6{background-color:#b3b7ff}table>*>tr.hintergrundfarbe7>th,table>*>tr>th.hintergrundfarbe7,table.hintergrundfarbe7,.hintergrundfarbe7{background-color:#ffcbcb}table>*>tr.hintergrundfarbe8>th,table>*>tr>th.hintergrundfarbe8,table.hintergrundfarbe8,.hintergrundfarbe8{background-color:#ffebad}table>*>tr.hintergrundfarbe9>th,table>*>tr>th.hintergrundfarbe9,table.hintergrundfarbe9,.hintergrundfarbe9{background-color:#b9ffc5}sup.reference{font-style:normal;font-weight:400}sup,sub{line-height:1em}ol.references>li:target,sup.reference:target{background:#def}ol.references li a[href|="#cite_ref"]{font-style:italic}ol.references li div.sisterproject{display:inline}div#mw-missingcommentheader b{color:#900}div#mw-anon-edit-warning,div#mw-anon-preview-warning,div#mw-missingsummary,div#wp_talkpagetext{background:#d3e1f2;border:1px solid #1a47ff;margin:1em auto;padding:1em;width:80%}div#mw-content-text a.external[href^="//de.wikipedia.org"],div#mw-content-text a.external[href^="http://de.wikipedia.org"],div#mw-content-text a.external[href^="https://de.wikipedia.org"],div#mw-content-text a.external[href^="//toolserver.org"],div#mw-content-text a.external[href^="http://toolserver.org"],div#mw-content-text a.external[href^="https://toolserver.org"],div#mw-content-text a.external[href^="//tools.wmflabs.org"],div#mw-content-text a.external[href^="http://tools.wmflabs.org"],div#mw-content-text a.external[href^="https://tools.wmflabs.org"]{background:none;padding-right:0}.mw-summarymissed{border:5px solid red;padding:2px}div#editpage-copywarn{background:#fff;border:1px solid #c00000;font-size:90%}.toclimit-2 .toclevel-1 ul,.toclimit-3 .toclevel-2 ul,.toclimit-4 .toclevel-3 ul,.toclimit-5 .toclevel-4 ul,.toclimit-6 .toclevel-5 ul,.toclimit-7 .toclevel-6 ul{display:none}span.tocnumber{margin-right:0.3em}ul + .toc,ol + .toc{margin-top:0.5em}#commons-icon,#coordinates,#editcount,#issnlink,#shortcut,#spoken-icon,.topicon{display:none}.geo{display:none}div#p-lang li.FA{list-style-image:url(http://upload.wikimedia.org/wikipedia/commons/d/d0/Monobook-bullet-star-transparent.png)}div#p-lang li.GA{list-style-image:url(http://upload.wikimedia.org/wikipedia/commons/a/a1/Monobook-bullet-star-gray.png)}div#mw-subcategories,div#mw-pages,div#mw-category-media{clear:both}.imagemap-inline div{display:inline}td#wpDestFile-warning ul{border:1px solid red;padding:1.5em}textarea#wpUploadDescription{height:20em}.mw-titleprotectedwarning{background:#eee;border:2px solid red;padding:1em}.mw-editinginterface{background:#f9f9f9;border:1px solid #c00000;padding:2px}div#specialchars{background:white;border:1px solid #aaa;margin-top:3px;padding:1px;text-align:left}.mw-history-legend{background:#f9f9f9;border:1px solid #e9e9e9;clear:both;font-size:90%;margin:2px 0;padding:0 5px 5px}abbr{border-bottom-color:#ccc;border-bottom-color:rgba(75%,75%,75%,.5)}abbr:hover{border-bottom-color:inherit;border-bottom-color:currentColor}.sp-cached{background:#ffffe0 url(http://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Clock_and_warning.svg/20px-Clock_and_warning.svg.png) no-repeat 5px 3px;border:1px solid #eeee80;color:#606000;font-style:italic;margin:0.3em 0;padding:4px 0 4px 30px}.IPA a{text-decoration:none}* html .polytonic{font-family:"Arial Unicode MS","Palatino Linotype",Code2000,"New Athena Unicode","Gentium Plus",Gentium,"Athena Unicode"}* html .IAST{font-family:Code2000,SunExtA,"Arial Unicode MS",sans-serif}.Unicode{font-family:Code2000,Sun-ExtA,"Arial Unicode MS",NSimSun,sans-serif}.Unicode1{font-family:Code2001,Quivira,"MPH 2B Damase",sans-serif}.Unicode2{font-family:Sun-ExtB,Code2002,sans-serif}.IPA{font-family:Quivira,Code2000,Sun-ExtA,"DejaVu Sans","Gentium Plus",Gentium,"Doulos SIL",Helvetica,"Arial Unicode MS","Lucida Sans Unicode",sans-serif}.hebrew{font-family:Quivira,Sun-ExtA,"Arial Unicode MS","SBL Hebrew",Code2000,"MPH 2B Damase",sans-serif}.spanAr{font-family:"Arial Unicode MS",Scheherazade,Code2000,"DejaVu Sans",sans-serif}.music-symbol{font-family:"Musical Symbols",Euterpe,Code2001,sans-serif}.Unicode,.Unicode1,.Unicode2,.IPA,.hebrew,.spanAr,.music-symbol{font-family:inherit}.fr-watchlist-pending-notice{background:transparent;border:none;margin:0;padding:0}.fr-comment-box{display:none}.mw-fr-reviewlink{background:transparent}#mw-fr-revisiondetails-wrapper{z-index:1}.patrollink{display:none}.mw-special-Watchlist .mw-rollback-link{display:none}.action-view.page-Wikipedia_Hauptseite h1.firstHeading,.action-view.page-Wikipedia_Hauptseite #contentSub,.page-Wikipedia_Hauptseite #catlinks{display:none}#hauptseite h2{background:#d8e8ff;border:1px solid #8898bf;font-size:1em;font-weight:bold;margin:0;padding:0.1em 0}#hauptseite .inhalt{background:#fff;border:1px solid #8898bf;border-top:0;min-height:0;padding:0.3em 0.8em 0.4em}#hauptseite .inhalt hr{background:#8898bf;color:#8898bf;height:1px;margin:0.5em 0}#hauptseite .inhalt .mehr{clear:both;font-size:95%;margin-top:0.8em;text-align:right}.hauptseite-oben,.hauptseite-links,.hauptseite-rechts{margin-bottom:1em}.hauptseite-links{margin-right:0.5em}.hauptseite-rechts{margin-left:0.5em}.hauptseite-oben h2,.hauptseite-unten h2{text-align:center}.hauptseite-oben .inhalt .portale{font-weight:bold;margin:0.2em 0}.hauptseite-oben .inhalt .intern{font-size:90%;text-align:center}.hauptseite-links h2,.hauptseite-rechts h2{text-indent:0.8em}#hauptseite-schwesterprojekte .inhalt a{font-weight:bold}#coordinates,#editcount,#issnlink,#shortcut{display:block;font-size:x-small;line-height:1;position:absolute;right:0;text-align:right;text-indent:0;top:-1.4em;white-space:nowrap}div.topicon{float:right;font-size:0.8em;line-height:1;margin-left:3px}#firstHeading{overflow:visible}#jump-to-nav{position:absolute;top:-9999px}html{font-size:100%}@media print{div.NavFrame,div.BoxenVerschmelzen{display:none}span.mw-cite-backlink{display:none}#content .plainlinks-print a.external.text:after,#content .plainlinks-print a.external.autonumber:after{content:""}}/**/</style>'
_STYLE += u'<style style="display:none">td {text-align: center; width: 24pt} i {color: silver;}</style>'

def htmledChar(char):
    UNDEFINED = u'<i color="silver">?</i>'
    if not char:
        result = UNDEFINED
    elif char in _UNPRINTABLE_TO_NAME_MAP:
        result = u'<i color="silver">' + _UNPRINTABLE_TO_NAME_MAP[char] + u'</i/>'
    else:
        result = cgi.escape(char)
    return result


def createIbmCodes(name):
    descriptionPath = os.path.join('/home/roskakori/Downloads', name + '.txt')
    index = 0
    indexToCodeMap = {}
    with open(descriptionPath, 'rb') as descriptionFile:
        for lineNumber, line in enumerate(descriptionFile, start=1):
            line = line.strip('\n\r').strip()
            try:
                if (line != '') and (line[0] in string.hexdigits):
                    codeText = line.split()[0]
                    code = int(codeText, 16)
                    assert index not in indexToCodeMap
                    indexToCodeMap[index] = chr(code)
            except Exception, error:
                raise ValueError(u'%s:%d: %s' % (os.path.basename(descriptionPath), lineNumber, error))
            print '%3d: %r' % (index, indexToCodeMap.get(index))
            index += 1
    result = [indexToCodeMap.get(index, None) for index in xrange(256)]
    assert len(result) == 256
    return result


def createEncodingCodes(encoding, count=256):
    result = []
    for index in xrange(count):
        try:
            char = chr(index).decode(encoding)
        except UnicodeDecodeError, error:
            if '<undefined>' in ('%s' % error):
                char = None
            else:
                raise
        result.append(char)
    return result
   

def buildHtmlFromCodes(name, codes):
    targetPath = name + '.html'
    _log.info(u'write "%s"', targetPath)
    with codecs.open(targetPath, 'w', 'utf8') as htmlFile:
        code = 0
        htmlFile.write(u'<!DOCTYPE html>' + os.linesep)
        htmlFile.write(u'<html><head>' + os.linesep)
        htmlFile.write(u'<meta charset="utf-8"></meta>' + os.linesep)
        htmlFile.write(u'<title>%s</title>' % name + os.linesep)
        htmlFile.write(_STYLE + os.linesep)
        htmlFile.write(u'</head><body>' + os.linesep)
        htmlFile.write(u'<table class="prettytable">' + os.linesep)
        htmlFile.write(u'<tr>' + os.linesep)
        htmlFile.write(u'<td></td>' + os.linesep)
        for hexDigit in xrange(16):
            htmlFile.write(u'<th bgcolor="silver">%X</th>' % hexDigit + os.linesep)
        htmlFile.write(u'</tr>' + os.linesep)
        for rowIndex in xrange(len(codes) / 16):
            htmlFile.write(u'<tr>' + os.linesep)
            htmlFile.write(u'<th bgcolor="silver">%X_</th>' % rowIndex + os.linesep)
            for columnIndex in xrange(16):
                index = 16 * rowIndex + columnIndex
                char = codes[index]
                #print '%d: %r' % (index, char)
                char = htmledChar(char)
                lineToWrite = u'<td>%s</td>' % char + os.linesep
                htmlFile.write(lineToWrite)
            htmlFile.write(u'</tr>' + os.linesep)
        htmlFile.write(u'</table>' + os.linesep)
        htmlFile.write(u'</html>' + os.linesep)


def buildHtmlFromIbmCodes(name):
    codes = createIbmCodes(name)
    print codes
    buildHtmlFromCodes(name, codes)


def buildHtmlFromEncoding(encoding, count=256):
    codes = createEncodingCodes(encoding, count)
    buildHtmlFromCodes(encoding, codes)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    #buildHtmlFromIbmCodes('CP00273')
    #buildHtmlFromIbmCodes('CP00500')
    #buildHtmlFromIbmCodes('CP01141')
    buildHtmlFromEncoding('ascii', 128)
    buildHtmlFromEncoding('iso-8859-1')
    buildHtmlFromEncoding('iso-8859-15')
    #buildHtmlFromEncoding('cp273')
    buildHtmlFromEncoding('cp500')
    buildHtmlFromEncoding('cp1252')
