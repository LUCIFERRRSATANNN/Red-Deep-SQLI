import os,sys,random,time
import pyfiglet 

print('\033[36m')

result = pyfiglet.figlet_format("Red Deep SQLI ") 
print(result) 


# import pyfiglet module 
import pyfiglet 

print('\033[36m')

result = pyfiglet.figlet_format("DEV BY 𝙻𝚞𝚌𝚒𝚏𝚎𝚛.", font = "bubble" ) 
print(result) 


print('\033[0m')

print('\033[33m')

print("Do not forget to add the symbol (') at the end of the url to display the flaw on the site !") 

print('\033[32m')

sqli=['[vulnérable] http://www.fastfwd.nl/index.php?id=36' ,'[vulnérable] http://www.lacouleurdesjours.ch/sommaires.php?ID=36' ,'[vulnérable] https://www.skystartravels.com/gallery.php?id=1','[vulnérable] https://www.delhijainschool.com/gallery.php?id=15' ,'[vulnérable] http://www.christhujyothi.com/gallery.php?id=2' ,\
'[vulnérable] http://www.kelanadmc.com/slideshow/gallery.php?id=37' ,'[vulnérable] https://www.chefschoicecatering.com/gallery.php?id=9' ,'[vulnérable] https://www.nicksnestholyoke.com/gallery.php?id=18' ,'[vulnérable] http://christian-fischer.fr/gallery.php?id=16' ,'[vulnérable] http://www.meggieschneider.com/php/detail.php?id=48' ,\
'[vulnérable] http://www.belbana.com/our-products-detail.php?id=7' ,'[vulnérable] http://www.microtechinno.com/product/detail.php?id=34' ,'[vulnérable] http://www.embryohotel.com/room-detail.php?id=27' ,'[vulnérable] https://www.artt.edu.pk/faculty-detail.php?id=20' ,'[vulnérable] http://www.stewartandsmart.co.uk/car-detail.php?id=7' ,\
'[vulnérable] http://www.itproserv.net/pcconfigurator/cart.php?computer_type=preconfiguration&id=1' ,'[vulnérable] http://www.acr-renault.fr/partenaire.php?id=38' ,'[vulnérable] http://www.embryohotel.com/room-detail.php?id=27' ,'[vulnérable] http://www.sportsfanaticphotography.com/show_cart.php?id=81' ,'[vulnérable] https://www.aquatec-shop.com/shop_fr/achat/index.php?id=31' ,\
'[vulnérable] http://www.theRed Deeppetals.com/subcat1.php?cid=13' ,'[vulnérable] http://www.fbs-intl.com/category.php?cid=1' ,'[vulnérable] http://www.embryohotel.com/room-detail.php?id=27' ,'[vulnérable] http://www.sportsfanaticphotography.com/show_cart.php?id=81' ,'[vulnérable] https://www.aquatec-shop.com/shop_fr/achat/index.php?id=31' ,\
'[vulnérable] http://www.mcdracing.com/news.php?news=30' ,'[vulnérable] http://mohitminerals.in/news.php?id=27' ,'[vulnérable] http://www.interaliaproject.com/news.php?id=115' ,'[vulnérable] http://www.taiwah.com.sg/news.php?ID=2' ,'[vulnérable] https://www.crom.co.uk/news.php?id=1' ,\
'[vulnérable] http://www.issclan.it/ultrastats-0.3.16/ultrastats/src/rounds-detail.php?id=60261' ,'[vulnérable] https://eng.libertylines.it/news-detail.php?id=3742' ,'[vulnérable] http://www.stepgate.it/education/detail.php?id=21' ,'[vulnérable] https://www.visiole.fr/fr/boutique/review.php?id=30' ,\
'[GOV vulnérable] https://www.huainang.go.th/datacenter/detail.php?news_id=257' ,'[GOV vulnérable] https://www.tanoddoun.go.th/datacenter/detail.php?news_id=291' ,'[GOV vulnérable] https://www.suankan.go.th/datacenter/detail.php?news_id=1149' ,'[GOV vulnérable] https://www.bangtorad.go.th/datacenter/detail.php?news_id=136' ,\
'[GOV vulnérable] https://www.rommuang.go.th/datacenter/detail.php?news_id=507' ,'[GOV vulnérable] https://www.namhak.go.th/datacenter/detail.php?news_id=481' ,'[GOV vulnérable] https://www.aownoi.go.th/datacenter/detail.php?news_id=596' ,'[GOV vulnérable] https://www.thasamed.go.th/datacenter/detail.php?news_id=159' ,\
'[GOV vulnérable] https://pokkrongnakhon.com/datacenter/detail.php?news_id=3412' ,'[GOV vulnérable] https://www.dopatrang.go.th/datacenter/detail.php?news_id=42' ,'[GOV vulnérable] https://www.nareng.go.th/datacenter/detail.php?news_id=550' ,'[GOV vulnérable] https://www.saerhung.go.th/datacenter/detail.php?news_id=1504' ,\
'[GOV vulnérable] https://www.saotong.go.th/datacenter/detail.php?news_id=241' ,'[GOV vulnérable] https://www.chalong.go.th/datacenter/detail.php?news_id=1523' ,'[GOV vulnérable] https://www.khaophrabat.go.th/datacenter/detail.php?news_id=417' ,'[GOV vulnérable] https://www.thadee.go.th/datacenter/detail.php?news_id=1776' ,\
'[GOV vulnérable] https://www.la-ai.go.th/datacenter/detail.php?news_id=678' ,'[GOV vulnérable] https://bangnumjued.go.th/datacenter/detail.php?news_id=151' ,'[GOV vulnérable] https://www.nakhonphc.go.th/datacenter/detail.php?news_id=227' ,'[GOV vulnérable] https://www.karaked.go.th/datacenter/detail.php?news_id=684' ,\
'[vulnérable] https://icdq.al/site/mat.php?lang=1&idm=19&idr=8' ,'[vulnérable] https://www.huaiyotcoop.com/datacenter/detail.php?news_id=200' ,'[vulnérable] ttp://www.jagoclient.com/content.php?id=9' ,'[vulnérable] http://e3e5.com/author.php?id=6' ,\
'[GOV vulnérable] http://www.arkansas.gov/artowing/search/search.php?DETAIL=1' ,'[vulnérable] http://www.agencerare.fr/php/ressources/diaporama/index.php?uid=9' ,'[vulnérable] ttp://aiman.s.free.fr/index.php?cat=6' ,'[vulnérable] http://www.farmanew.com/infocaps.php?id=9078' ,'[vulnérable] https://www.ccomocine.com/shop/description.php?id=628' ,'[vulnérable] http://www.xtraconchessopen.dk/index.php?uid=9' ,\
'[GOV vulnérable] https://www.ronthongcity.go.th/datacenter/detail.php?news_id=561' ,'[GOV vulnérable] https://www.maechaoyuhou.go.th/datacenter/detail.php?news_id=1330' ,'[GOV vulnérable] https://www.khuanthani.go.th/datacenter/detail.php?news_id=1140' ,'[GOV vulnérable] https://www.yarom.go.th/datacenter/detail.php?news_id=323' ,\
'[GOV vulnérable] https://www.kalupank.go.th/datacenter/detail.php?news_id=397' ,'[GOV vulnérable] https://www.thapaya.go.th/datacenter/detail.php?news_id=1' ,'[GOV vulnérable] https://malt.pw.usda.gov/t3/sandbox/wheat/genotyping/show.php?line=4971' ,'[vulnérable] https://www.mshornipolice.cz/public/printAction.php?id=193' ,\
'[GOV vulnérable] http://tangua.rj.gov.br/mapadecrimes/dados/index.php?id=1' ,'[GOV vulnérable] https://www.camarasalete.sc.gov.br/vereador' ,'[vulnérable] https://www.turismo.sp.gov.br/1364?id=1' ,'[GOV vulnérable] http://heritage.nv.gov/species/process.php?id=1' ,'[vulnérable] https://www.crom.co.uk/news.php?id=1']

random.shuffle(sqli) # shuffle before print 
for ins in sqli:
	print ins
	time.sleep (.3)

