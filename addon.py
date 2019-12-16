from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon
plugin = Plugin()
url1 = "https://feeds.megaphone.fm/slatesthegist"
url2 = "https://feeds.megaphone.fm/whatnext"
url3 = "https://feeds.megaphone.fm/slatemoney"
url4 = "https://feeds.megaphone.fm/slatespoliticalgabfest"
url5 = "http://feeds.megaphone.fm/watergate"
url6 = "https://feeds.megaphone.fm/trumpcast"
url7 = "https://feeds.megaphone.fm/slateswhistlestop"
url8 = "https://feeds.megaphone.fm/slatesamicuswithdahlialithwick"
url9 = "https://feeds.megaphone.fm/hisdarkmaterials"
url10 = "https://feeds.megaphone.fm/slatesculturegabfest"
url11 = "https://feeds.megaphone.fm/slatesspoilerspecials"
url12 = "https://feeds.megaphone.fm/slateshangupandlisten"
url13 = "http://feeds.megaphone.fm/hitparade"
url14 = "http://feeds.feedburner.com/studio360/podcast"
url15 = "https://feeds.megaphone.fm/SLT6483094633"
url16 = "https://feeds.megaphone.fm/historyofthefuture"
url17 = "http://feeds.megaphone.fm/ifthen"
#url18 = "https://feeds.megaphone.fm/slatemoney"
url19 = "https://feeds.megaphone.fm/slatesworking"
url20 = "https://feeds.megaphone.fm/SM3958815784"
url21 = "https://feeds.megaphone.fm/hiphination"
url22 = "https://feeds.megaphone.fm/SLT1859464427"
url23 = "https://feeds.megaphone.fm/slatelexiconvalley"
url24 = "https://feeds.megaphone.fm/aymann"
url25 = "https://feeds.megaphone.fm/slatesmomanddadarefighting"
url26 = "https://feeds.megaphone.fm/outward"
url27 = "http://feeds.megaphone.fm/slatesdoublexpodcasts?limit=900"
url28 = "https://feeds.megaphone.fm/represent"
url29 = "https://www.omnycontent.com/d/playlist/aaea4e69-af51-495e-afc9-a9760146922b/8f57a588-9582-4b05-89c9-aaa001627e6f/5e92c398-71a9-4767-8181-aaa001627e86/podcast.rss"
url30 = "https://feeds.megaphone.fm/SLT1725950547"
url31 = "https://feeds.megaphone.fm/ask"
url32 = "https://feeds.megaphone.fm/SLT9749984441"
url33 = "https://feeds.megaphone.fm/slatesworking"
url34 = "https://feeds.megaphone.fm/slatesaudiobookclub"

@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001),
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://megaphone.imgix.net/podcasts/322754a0-8289-11e5-b42a-9768945f372d/image/uploads_2F1516106554073-8qgavf6rjq8-a63340bf37b427df31e62e0440cc0294_2F01_Slate_Redux_Podcast_Cover_The-Gist.jpg?w=263&h=263"},
        {
            'label': plugin.get_string(30002),
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://megaphone.imgix.net/podcasts/64c7c85e-c7f5-11e8-9628-33972ffbe22a/image/uploads_2F1539377262546-95sbl4uxijh-bf33a43e0c2a94ab42f4ed70fea47128_2Fwhat-next-tile-3000px.jpg?w=263&h=263"},
        {
            'label': plugin.get_string(30003),
            'path': plugin.url_for('episodes3'),
            'thumbnail': "https://megaphone.imgix.net/podcasts/3244f352-8289-11e5-b42a-730ed12c5ae6/image/uploads_2F1516105165439-3mqt15g4y3d-2c496fccbc1a29b938303b2bda12467a_2F01_Slate_Redux_Podcast_Cover_Slate-Money.jpg?w=263&h=263"},
        {
            'label': plugin.get_string(30004),
            'path': plugin.url_for('episodes4'),
            'thumbnail': "https://megaphone.imgix.net/podcasts/310f8cfe-8289-11e5-b42a-c78a2a468812/image/uploads_2F1516104874974-9xwrsh4ccl-5e5f7491cf0582599bb2341880f5eff8_2F01_Slate_Redux_Podcast_Cover_Political-Gabfest.jpg?w=263&h=263"},
        {
            'label': plugin.get_string(30005),
            'path': plugin.url_for('episodes5'),
            'thumbnail': "https://megaphone.imgix.net/podcasts/72206cba-ffdd-11e9-bcf3-4b1aff9109b8/image/uploads_2F1572966215773-lmeqvgv6cjn-8a7620c0bc586557135f31876e8c6210_2Fuploads_2F1564165061806-hip7w19g0h4-5d1488ba0594b2d85671d2534b34cbb0_2Fslow_burn_3000.jpg?w=263&h=263"},
        {
            'label': plugin.get_string(30006),
            'path': plugin.url_for('episodes6'),
            'thumbnail': "https://is3-ssl.mzstatic.com/image/thumb/Podcasts113/v4/8e/b3/d2/8eb3d234-d485-395b-2aa1-bb5ba571844c/mza_2076228034282578772.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30007),
            'path': plugin.url_for('episodes7'),
            'thumbnail': "https://is5-ssl.mzstatic.com/image/thumb/Podcasts123/v4/ed/36/29/ed36299c-d27a-d870-9369-cbdaac94800a/mza_9216844687241586990.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30008),
            'path': plugin.url_for('episodes8'),
            'thumbnail': "https://megaphone.imgix.net/podcasts/32590f9a-8289-11e5-b42a-071d65eb13b2/image/uploads_2F1516131500056-g2cl5bp0giu-86bb34c4a8ac94ff6a6aa04e6bf665f5_2F01_Slate_Redux_Podcast_Cover_AmicusDahlia.jpg?w=263&h=263"},
        {
            'label': plugin.get_string(30009),
            'path': plugin.url_for('episodes9'),
            'thumbnail': "https://is2-ssl.mzstatic.com/image/thumb/Podcasts113/v4/19/41/ca/1941ca7c-6283-98fb-b6cf-4f2c2030f554/mza_13773143939701545694.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30010),
            'path': plugin.url_for('episodes10'),
            'thumbnail': "https://is4-ssl.mzstatic.com/image/thumb/Podcasts113/v4/12/21/8c/12218c4b-fd5a-50d6-a13f-aebc53b596b6/mza_14096405403423493949.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30011),
            'path': plugin.url_for('episodes11'),
            'thumbnail': "https://megaphone-prod.s3.amazonaws.com/podcasts/30ad81f8-8289-11e5-b42a-a339e1fc57f0/image/uploads_2F1516105089792-vq7id2m12ca-7a3491617ebbed510296ef968d4d7cd4_2F01_Slate_Redux_Podcast_Cover_Spoiler-Specials.jpg"},
        {
            'label': plugin.get_string(30012),
            'path': plugin.url_for('episodes12'),
            'thumbnail': "https://megaphone-prod.s3.amazonaws.com/podcasts/315f6030-8289-11e5-b42a-cb184c69d8df/image/uploads_2F1516105977185-m7u47vx5e2h-ec07a24d54312dd61910a3053264fb02_2F01_Slate_Redux_Podcast_Cover_Hang-Up-And-Listen.jpg"},
        {
            'label': plugin.get_string(30013),
            'path': plugin.url_for('episodes13'),
            'thumbnail': "https://is5-ssl.mzstatic.com/image/thumb/Podcasts123/v4/2f/fb/a8/2ffba890-b6fb-4c79-7fc9-d335f88fb351/mza_2378843336221009205.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30014),
            'path': plugin.url_for('episodes14'),
            'thumbnail': "https://is1-ssl.mzstatic.com/image/thumb/Podcasts113/v4/00/a1/ca/00a1ca34-f3a8-be94-c5a0-ce1e143c83a0/mza_11298508720511783865.png/600x600bb.jpg"},
        {
            'label': plugin.get_string(30015),
            'path': plugin.url_for('episodes15'),
            'thumbnail': "https://is4-ssl.mzstatic.com/image/thumb/Podcasts113/v4/2a/a8/1e/2aa81ee2-edb0-cd05-a294-72bf3cf06f45/mza_5746556637777446389.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30016),
            'path': plugin.url_for('episodes16'),
            'thumbnail': "https://is3-ssl.mzstatic.com/image/thumb/Podcasts113/v4/f8/c2/94/f8c294c3-ca7e-3a3a-6e09-72931f8b571b/mza_5105868252812787015.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30017),
            'path': plugin.url_for('episodes17'),
            'thumbnail': "https://is3-ssl.mzstatic.com/image/thumb/Podcasts113/v4/f1/93/19/f1931958-1a8f-8701-40f9-589a5078ad04/mza_11635932876957282012.jpg/600x600bb.jpg"},
#        {
#            'label': plugin.get_string(30018),
#            'path': plugin.url_for('episodes18'),
#            'thumbnail': "https://is2-ssl.mzstatic.com/image/thumb/Podcasts123/v4/90/12/41/90124115-44f0-32f1-867e-510724ee7c84/mza_7202452206247679366.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30019),
            'path': plugin.url_for('episodes19'),
            'thumbnail': "https://is3-ssl.mzstatic.com/image/thumb/Podcasts113/v4/8c/40/a7/8c40a7c8-d7d8-a5f3-3949-b30532b87444/mza_41680801910960999.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30020),
            'path': plugin.url_for('episodes20'),
            'thumbnail': "https://is4-ssl.mzstatic.com/image/thumb/Podcasts123/v4/80/e8/80/80e88065-518c-5ca0-d1fa-a1a01b8d422b/mza_130572933403987461.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30021),
            'path': plugin.url_for('episodes21'),
            'thumbnail': "https://is5-ssl.mzstatic.com/image/thumb/Podcasts123/v4/bc/a3/52/bca352a5-95ab-efd0-625f-d892fc3e4c49/mza_5488251342726134281.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30022),
            'path': plugin.url_for('episodes22'),
            'thumbnail': "https://is3-ssl.mzstatic.com/image/thumb/Podcasts123/v4/20/08/e3/2008e397-0561-1f04-0d03-3a138c6b220f/mza_3771371304287194869.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30023),
            'path': plugin.url_for('episodes23'),
            'thumbnail': "https://is3-ssl.mzstatic.com/image/thumb/Podcasts123/v4/c0/26/2b/c0262bd2-a773-e0d7-a9b3-03466fc301f3/mza_675697409414569355.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30024),
            'path': plugin.url_for('episodes24'),
            'thumbnail': "https://is2-ssl.mzstatic.com/image/thumb/Podcasts123/v4/ff/db/aa/ffdbaa24-441e-6c28-af16-dc62de13b0b6/mza_361566432009760239.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30025),
            'path': plugin.url_for('episodes25'),
            'thumbnail': "https://is1-ssl.mzstatic.com/image/thumb/Podcasts123/v4/60/df/1d/60df1d3c-78da-9420-6aaf-eff85952a5db/mza_4901003220313463570.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30026),
            'path': plugin.url_for('episodes26'),
            'thumbnail': "https://is5-ssl.mzstatic.com/image/thumb/Podcasts113/v4/b2/fd/c7/b2fdc7fe-710b-441e-78e0-9d626cc85928/mza_9101833446204054481.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30027),
            'path': plugin.url_for('episodes27'),
            'thumbnail': "https://is2-ssl.mzstatic.com/image/thumb/Podcasts113/v4/23/93/18/2393183f-2783-2287-2a2c-cfcc088469c3/mza_6550972113947727044.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30028),
            'path': plugin.url_for('episodes28'),
            'thumbnail': "https://is5-ssl.mzstatic.com/image/thumb/Podcasts123/v4/ec/6e/28/ec6e28d4-d1d6-5b8a-1acf-8ea057fa06f1/mza_2516576784225614591.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30029),
            'path': plugin.url_for('episodes29'),
            'thumbnail': "https://is3-ssl.mzstatic.com/image/thumb/Podcasts123/v4/d4/34/0c/d4340cef-7d28-32c9-a31f-f50c79560f52/mza_2719386742701717516.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30030),
            'path': plugin.url_for('episodes30'),
            'thumbnail': "https://is5-ssl.mzstatic.com/image/thumb/Podcasts123/v4/4b/ac/82/4bac824d-b01d-b95c-995b-fb7edb8ed78f/mza_6293008322535068240.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30031),
            'path': plugin.url_for('episodes31'),
            'thumbnail': "https://is3-ssl.mzstatic.com/image/thumb/Podcasts123/v4/84/b8/eb/84b8eb36-e144-4746-c694-32306a537804/mza_1125258124883782489.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30032),
            'path': plugin.url_for('episodes32'),
            'thumbnail': "https://is1-ssl.mzstatic.com/image/thumb/Podcasts123/v4/ed/c2/2d/edc22dbd-53d2-5beb-e40b-224e41416cce/mza_4200380185631344954.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30033),
            'path': plugin.url_for('episodes33'),
            'thumbnail': "https://is3-ssl.mzstatic.com/image/thumb/Podcasts113/v4/8c/40/a7/8c40a7c8-d7d8-a5f3-3949-b30532b87444/mza_41680801910960999.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30034),
            'path': plugin.url_for('episodes34'),
            'thumbnail': "https://megaphone.imgix.net/podcasts/30836968-8289-11e5-b42a-8b58d75e4327/image/uploads_2F1516106489105-h4f6038a6p-fa3e6d340872c743db8217528232fb09_2F01_Slate_Redux_Podcast_Cover_Audio-Book-Club.jpg?w=350&h=350"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items
@plugin.route('/episodes2/')
def episodes2():
    soup2 = mainaddon.get_soup2(url2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items
@plugin.route('/episodes3/')
def episodes3():
    soup3 = mainaddon.get_soup3(url3)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup3)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items
@plugin.route('/episodes4/')
def episodes4():
    soup4 = mainaddon.get_soup4(url4)   
    playable_podcast4 = mainaddon.get_playable_podcast4(soup4)
    items = mainaddon.compile_playable_podcast4(playable_podcast4)
    return items
@plugin.route('/episodes5/')
def episodes5():
    soup5 = mainaddon.get_soup5(url5)
    playable_podcast5 = mainaddon.get_playable_podcast5(soup5)
    items = mainaddon.compile_playable_podcast5(playable_podcast5)
    return items
@plugin.route('/episodes6/')
def episodes6():
    soup6 = mainaddon.get_soup6(url6)
    playable_podcast6 = mainaddon.get_playable_podcast6(soup6)
    items = mainaddon.compile_playable_podcast6(playable_podcast6)
    return items
@plugin.route('/episodes7/')
def episodes7():
    soup7 = mainaddon.get_soup7(url7)
    playable_podcast7 = mainaddon.get_playable_podcast7(soup7) 
    items = mainaddon.compile_playable_podcast7(playable_podcast7)
    return items
@plugin.route('/episodes8/')
def episodes8():
    soup8 = mainaddon.get_soup8(url8)
    playable_podcast8 = mainaddon.get_playable_podcast8(soup8)
    items = mainaddon.compile_playable_podcast8(playable_podcast8)
    return items
@plugin.route('/episodes9/')
def episodes9():
    soup9 = mainaddon.get_soup9(url9)
    playable_podcast9 = mainaddon.get_playable_podcast9(soup9)
    items = mainaddon.compile_playable_podcast9(playable_podcast9)
    return items
@plugin.route('/episodes10/')
def episodes10():
    soup10 = mainaddon.get_soup10(url10)
    playable_podcast10 = mainaddon.get_playable_podcast10(soup10)
    items = mainaddon.compile_playable_podcast10(playable_podcast10)
    return items
@plugin.route('/episodes11/')
def episodes11():
    soup11 = mainaddon.get_soup11(url11)
    playable_podcast11 = mainaddon.get_playable_podcast11(soup11)
    items = mainaddon.compile_playable_podcast11(playable_podcast11)
    return items
@plugin.route('/episodes12/')
def episodes12():
    soup12 = mainaddon.get_soup12(url12) 
    playable_podcast12 = mainaddon.get_playable_podcast12(soup12)
    items = mainaddon.compile_playable_podcast12(playable_podcast12)
    return items
@plugin.route('/episodes13/')
def episodes13():
    soup13 = mainaddon.get_soup13(url13)
    playable_podcast13 = mainaddon.get_playable_podcast13(soup13)
    items = mainaddon.compile_playable_podcast13(playable_podcast13)
    return items
@plugin.route('/episodes14/')
def episodes14():
    soup14 = mainaddon.get_soup14(url14)
    playable_podcast14 = mainaddon.get_playable_podcast14(soup14)
    items = mainaddon.compile_playable_podcast14(playable_podcast14)
    return items
@plugin.route('/episodes15/')
def episodes15():
    soup15 = mainaddon.get_soup15(url15)
    playable_podcast15 = mainaddon.get_playable_podcast15(soup15)
    items = mainaddon.compile_playable_podcast15(playable_podcast15)
    return items
@plugin.route('/episodes16/')
def episodes16():
    soup16 = mainaddon.get_soup16(url16)
    playable_podcast16 = mainaddon.get_playable_podcast16(soup16)
    items = mainaddon.compile_playable_podcast16(playable_podcast16)
    return items
@plugin.route('/episodes17/')
def episodes17():
    soup17 = mainaddon.get_soup17(url17)
    playable_podcast17 = mainaddon.get_playable_podcast17(soup17)
    items = mainaddon.compile_playable_podcast17(playable_podcast17)
    return items
#@plugin.route('/episodes18/')
#def episodes18():
#    soup18 = mainaddon.get_soup18(url18)
#    playable_podcast18 = mainaddon.get_playable_podcast18(soup18)
#    items = mainaddon.compile_playable_podcast18(playable_podcast18)
#    return items
@plugin.route('/episodes19/')
def episodes19():
    soup19 = mainaddon.get_soup19(url19)
    playable_podcast19 = mainaddon.get_playable_podcast19(soup19)
    items = mainaddon.compile_playable_podcast19(playable_podcast19)
    return items
@plugin.route('/episodes20/')
def episodes20():
    soup20 = mainaddon.get_soup20(url20)
    playable_podcast20 = mainaddon.get_playable_podcast20(soup20)
    items = mainaddon.compile_playable_podcast20(playable_podcast20)
    return items
@plugin.route('/episodes21/')
def episodes21():
    soup21 = mainaddon.get_soup21(url21)
    playable_podcast21 = mainaddon.get_playable_podcast21(soup21)
    items = mainaddon.compile_playable_podcast21(playable_podcast21)
    return items
@plugin.route('/episodes22/')
def episodes22():
    soup22 = mainaddon.get_soup22(url22)
    playable_podcast22 = mainaddon.get_playable_podcast22(soup22)
    items = mainaddon.compile_playable_podcast22(playable_podcast22)
    return items
@plugin.route('/episodes23/')
def episodes23():
    soup23 = mainaddon.get_soup23(url23)
    playable_podcast23 = mainaddon.get_playable_podcast23(soup23)
    items = mainaddon.compile_playable_podcast23(playable_podcast23)
    return items
@plugin.route('/episodes24/')
def episodes24():
    soup24 = mainaddon.get_soup24(url24)
    playable_podcast24 = mainaddon.get_playable_podcast24(soup24)
    items = mainaddon.compile_playable_podcast24(playable_podcast24)
    return items
@plugin.route('/episodes24/')
def episodes25():
    soup25 = mainaddon.get_soup25(url25)
    playable_podcast25 = mainaddon.get_playable_podcast25(soup25)
    items = mainaddon.compile_playable_podcast25(playable_podcast25)
    return items
@plugin.route('/episodes26/')
def episodes26():
    soup26 = mainaddon.get_soup26(url26)
    playable_podcast26 = mainaddon.get_playable_podcast26(soup26)
    items = mainaddon.compile_playable_podcast26(playable_podcast26)
    return items
@plugin.route('/episodes27/')
def episodes27():
    soup27 = mainaddon.get_soup27(url27)
    playable_podcast27 = mainaddon.get_playable_podcast27(soup27)
    items = mainaddon.compile_playable_podcast27(playable_podcast27)
    return items
@plugin.route('/episodes28/')
def episodes28():
    soup28 = mainaddon.get_soup28(url28)
    playable_podcast28 = mainaddon.get_playable_podcast28(soup28)
    items = mainaddon.compile_playable_podcast28(playable_podcast28)
    return items
@plugin.route('/episodes29/')
def episodes29():
    soup29 = mainaddon.get_soup29(url29)
    playable_podcast29 = mainaddon.get_playable_podcast29(soup29)
    items = mainaddon.compile_playable_podcast29(playable_podcast29)
    return items
@plugin.route('/episodes30/')
def episodes30():
    soup30 = mainaddon.get_soup30(url30)
    playable_podcast30 = mainaddon.get_playable_podcast30(soup30)
    items = mainaddon.compile_playable_podcast30(playable_podcast30)
    return items
@plugin.route('/episodes31/')
def episodes31():
    soup31 = mainaddon.get_soup31(url31)
    playable_podcast31 = mainaddon.get_playable_podcast31(soup31)
    items = mainaddon.compile_playable_podcast31(playable_podcast31)
    return items
@plugin.route('/episodes32/')
def episodes32():
    soup32 = mainaddon.get_soup32(url32)
    playable_podcast32 = mainaddon.get_playable_podcast32(soup32)
    items = mainaddon.compile_playable_podcast32(playable_podcast32)
    return items
@plugin.route('/episodes33/')
def episodes33():
    soup33 = mainaddon.get_soup33(url33)
    playable_podcast33 = mainaddon.get_playable_podcast33(soup33)
    items = mainaddon.compile_playable_podcast33(playable_podcast33)
    return items
@plugin.route('/episodes34/')
def episodes34():
    soup34 = mainaddon.get_soup34(url34)
    playable_podcast34 = mainaddon.get_playable_podcast34(soup34)
    items = mainaddon.compile_playable_podcast34(playable_podcast34)
    return items
if __name__ == '__main__':
    plugin.run()
