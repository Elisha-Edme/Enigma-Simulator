import Enigma as eng
import unittest as uni

def create_enigma1(plug=eng.Plugboard()):
     return eng.Enigma(
        #### Rotors#####
        [eng.ENIGMA_SETTINGS["ENIGMA1 ROTOR 1"],
        eng.ENIGMA_SETTINGS["ENIGMA1 ROTOR 2"],
        eng.ENIGMA_SETTINGS["ENIGMA1 ROTOR 3"]],
        eng.ENIGMA_SETTINGS["ENIGMA1 REFLECTOR B"],
    plug)

# Formats tests and messages so that they can be more easily compared
# Takes out punctuation, whitespaces, and makes the string one case
def format(string):
    return string.replace(" ", '').replace(".", '').replace(",", '').replace('\n','').lower()
lipsum = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas porttitor est in condimentum interdum. Duis pellentesque tempus gravida. Ut vitae est leo. Vivamus purus orci, vehicula a suscipit ullamcorper, venenatis in neque. In eu ante mauris. Sed sollicitudin magna bibendum ultrices facilisis. Vivamus quis velit faucibus, hendrerit nulla eu, tincidunt ipsum.

Ut facilisis eleifend ante, quis pulvinar diam faucibus at. Aliquam ac aliquet enim, sed venenatis lectus. Ut ac risus in nulla condimentum rhoncus eget quis enim. Ut porttitor eu turpis eu efficitur. Phasellus condimentum eu est vulputate aliquet. Etiam eu tincidunt nulla. Aenean vestibulum vestibulum lacus varius placerat. Vivamus vehicula imperdiet mauris eu rhoncus. Nunc ac libero vel lectus varius tristique. Nullam facilisis tempus ligula ac porttitor. Phasellus consequat elit eu arcu semper facilisis. Duis sem nunc, hendrerit sagittis sollicitudin eget, tincidunt sed elit.

Morbi ornare venenatis tincidunt. Nulla sit amet bibendum ex. Quisque sed risus quis leo consectetur finibus ut id leo. Morbi sed dolor interdum, ullamcorper magna eget, tincidunt tortor. Vestibulum convallis enim ut dui ultrices rutrum. Suspendisse rutrum eleifend finibus. Suspendisse nec cursus eros. Pellentesque eget justo et nunc facilisis vestibulum. Vestibulum in elementum turpis. Nunc scelerisque diam a magna dignissim, nec pharetra nunc dictum. Nulla faucibus tellus ac pellentesque lacinia. Curabitur at velit tincidunt eros rutrum pulvinar at quis sem. Mauris rutrum malesuada rhoncus. Proin consequat eleifend egestas. Praesent interdum metus ut sapien consequat ultricies.

Suspendisse mollis lobortis sagittis. Integer congue nulla sapien, vel ullamcorper mauris sagittis eu. Etiam vel nisi lectus. Sed eu euismod quam, non feugiat odio. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris suscipit dictum lacus id eleifend. Proin et erat sapien. Vivamus ac ultricies lorem. Maecenas vestibulum metus ut eros venenatis ullamcorper. Aenean tincidunt turpis in interdum semper. Sed egestas euismod rhoncus. Integer eget ex non felis interdum malesuada vitae sit amet erat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.

In semper urna ac porta mattis. Aenean venenatis, metus condimentum vulputate vulputate, magna enim interdum metus, sit amet maximus magna diam at tellus. Nullam molestie felis id risus lobortis, sed malesuada lorem lobortis. Vestibulum cursus lacinia justo, quis porttitor quam vulputate ac. In ac diam gravida purus maximus tempor nec id diam. Sed justo ante, eleifend eget tempor nec, pharetra eu magna. Cras eleifend est molestie, faucibus justo mollis, faucibus tellus. Maecenas nec dignissim erat. Fusce eu nunc metus. Curabitur suscipit, ipsum in tincidunt suscipit, lacus sem tincidunt arcu, dapibus luctus massa neque non risus. Donec quis fringilla arcu. Ut finibus lectus in dui gravida, non commodo enim eleifend. Nunc metus ipsum, ultricies eget euismod ac, mollis ac augue. Nam nulla sapien, laoreet ac vulputate eu, aliquam accumsan nisl. Pellentesque in pretium enim, eu mattis elit. Proin semper enim finibus enim tincidunt, quis dapibus nibh mattis.'''
lipsum = lipsum.replace(",", "").replace(".", "")

'''
Uses Unittest to test '''

class TestEnigmaMethods(uni.TestCase):

    #@uni.skip("Already passed the normal encryption test")
    def test_encryption(self):
        Enigma1 = create_enigma1()
        message = 'the bois are catching up to me'
        message = format(message)
        ########## Tests a normal sentence ##################
        testOutput = "zptgz aaxxu lwbtq zbrmu aiwp"
        testOutput = format(testOutput)
        self.assertEqual(Enigma1.encrypt_message(message), testOutput)
        Enigma1.reset()
        ########### Stress tests a 5 paragraph lorem ipsum text ###############
        message = lipsum
        testOutput = '''ilfdf arubd onvis rukoz qmndi ycouh rlawb rmpyl aznyn grstn ixwpz elkjh leihy gynud jbwva trotf byjxx bhywe korrf wxdms txprw ntkba hcmfo hwkjo uhtyb qnvlv wandq gcurk etstj aftdn phpso nmjps xsqhg mclgp jshsu gojqq fpfjf clevp ltkey qzyhd qlvjm bnazx zbgvh mojkq iwqld ynjco kazqh jckvz qbyyb dopzp bzehw ycgew eprop ojthy pguic aitav bnvzo rkxrc uiazz nirte ykezq robwh lzuxm ncnwy jhrru irjtb ipqej kgeul odbqk uxxkk yppgl yvcpn ppjsf vhifr jywvx pykod vzdfh oysyh icxqv hoovm ahoxk wqhog xvzwj dfdrz uidob cpwlm mrjgm exuec mnqen imtfc ftqbp rrkyq vbjck uzbho pcsqo buejz vyglk zaiux assyi jgpzr mdyrl zirnk frtfi yhhme qilom hvhhk slxgm vjxac bmxln aukli cetnu fijae efykk ugytb xdxzf rvzqq gykem qbuou qlcrz vjxci ylfaq clzyf dryaq rxeda fxkui pwgvy lsnch ayzav vuuep jzvgg qsbtk vqlhs ouhzd ihtuj pkjty msalo zzucj ajqvb dwiqz kewua xjqnq qxskf xprza kalcv mensp zfcnx rppzr qxaod aurpu kfzzm ideuf zcmuj mnbyj gkggb bundm czuuw fbnan kyzkn vipmj hryxo quuyw rpkdx ocrpq ixvdb zbpbw nyeaw hqxie lwtup fywft blbfe jopqp bwyng bsydp lojcq annhf farjl ivjfb xgrlf ynypc hajhn kyirp zmxjs jvzym tixlt qpisk vhpfv lpvwh mzhjn zbaen dajnx gxyuz eajyu htdau diqfb gqyyb tusyj jgtys kqpgd duzcq bhcsh szkrw tonit xvzjl oogzg nuaum dcdzr azepy luqzg vdiuu razai wdbrz uodfd fjkmj vhbib ahosi rksgn rojsg qcorx hnzag eshxt grzhr dxojl xegbx aaovg gnueb ahfda gsigw eylpq tjtqe uxhlk kndcl azijj jptql wrdff wkpno dvwjy juerm ikutf ioecv iwtuf tcixn maluj agmyq fsltf fiyoz yzunt wdmqm buush kmmho cdadg rylhw zyfmz njscn ovfkz hahwo dtaee axowd zkqrc ejxva yucph ashrc ngcub eoupm alqiu ructo qaizb gfrnb vvahh ogwcw yisrr wtwxw slkks fovkt vevgz lfphw orrxs uhouj htaar prxrw dvmxq gsxle lszvs xzgvr zbqvb uafjk bcnzu nemyv glgpe ktmjp wyont zttoa cipda ycpmc jraer fzmnk fteth uorem elshp npywj enhhj hqssg sbepx zxcfw lnlzv mzxwc trxam dpmts cmotv flxhw bfxii owuhb jjrsj mvnfg klaxz qdpgd poynb wnfxu fwsxh chjdw rsjln aqtha oirnu iwuvr mkrpq cwtcr stthp fbpnb ypblw nbsqh qiivy djpxp qbgvj inzjx hqcas oifvh bwauq yyuic moxux wqtux aaykj mpgrt woqwo turqe xicag mdosa ebnlo kpxaq ucyuq ykehr kidcy cclqd orkww opxmu urujk ndnfq eyanp bswbt pdtvh jvnmb xjfex louvu wufff dskmm owczx foqpi hjumu cuuam axdbe xqhgh kkoep flsmy zlnti oonho endtf qmbby mqsrd bdnfi oholm ltwdx vgdyz cptfc yhpvv whfaj xftta kdrga mhgbz gonuk sckwk jhxre bzzev zlunu prdhi ajfkk nxogj vvyys fwzxf ruttb zkujm drekm ahsbr aufqi sgtdh bjcjt jaeur qwszc zchqe xtdfm rnrzr ymhnq wewoc uvzff ieojp ondab uzzbw okykr uxqdt lwslz mduwv quljs gxadi uwzqx fmovc rklbm zuaid gpkhj ifdet ddepl bzndw duiwf hgtiw wjvgc aewec xhrzt blrjx gqrsl dxtao idogy ujwca jrrrs yxwiz ikmck smbxa crenv rfnnu tyygw aeiwq cchuu paqnf qqmkp gkvcw apfuq vwdjt xlhip esecw ihoqv bgslm foqmp xdlfg inkdl tcdfp hfvxi wbtvk bqqyg lqdup qnlkm vwugr uaeec opihv qhipe bmhkf sudzt hutfp xryqm llrfd yuahd tdzno kypve lyawe iayhz cjewx qwgxt smvft spvow efzum oazjr yfvmv ctkpm tcxsz gxohg xounw dylvm lhgkl iracw cmzzr yrzcp vgobb vvdvs cdtdt iplbr rnsst sxskx dvxgx jqsnu heykg rzqzm cdsnk qoskm ysjol pebor xmolr aoivk ddxxo znqeg ygwch eikwx hrsyw uxjao zvlzf ztjkh jkyzg zlnyo hojyg yacux hjwcd grdch fropv ahpbr nrzjf nykio lxvmi qbj'''
        message = format(message)
        testOutput = format(testOutput)
        self.assertEqual(Enigma1.encrypt_message(message), testOutput)

    #@uni.skip("Already passed the offset test")
    def test_ringOffset(self):
        Enigma1 = create_enigma1()
        Enigma1.set_ring_offset(4, 0)
        ########## Tests a single character ##################
        message = 'c'
        message = format(message)
        testOutput = "x"
        testOutput = format(testOutput)
        print(Enigma1.rotors[0])
        self.assertEqual(Enigma1.encrypt_message(message), testOutput)
        Enigma1.reset()
        ########### Stress tests a 5 paragraph lorem ipsum text ###############
        Enigma1.set_ring_offset(16, 0)
        message = lipsum
        message = format(message)
        testOutput = format(
            '''qqqcb vlvny vzeyi xuuii bzuqh rszrb oigon dwvbp zpbxm cdzrs lamfg bkclw grten lccrz qwaqj dpxej xgvhf gzoak ghjle chzqa vcjke jwnmu ahvlo hppxd abdvm cmsxa wmaio iulmx oyqqp ybulb tgydz zpxfk steca kgada ykvgl lwnum ntmeq pyybm sojoq vwzsh qbvqx fphvh cuerm qkvcs jmomq cxvjs ixbbs qphah ksgdm rudop zqhxs xagyd alqwp myjfe pvdxv mjurb nbtgv uqzfu skxxb ztmdd zxyor adahh ucuoi xidxb tqrxw slilm kwjxh ugyno unmjj znffd ifdzc ortkl wqcom foyqs hnecj wtpzx wywcf lywsj fqyme yyofn pwmda oljax cewfs zzpcy fqmvl pzbig yxito roezj tupxx tojxs iwzgz uifxq nzmnn gayyo yjtbp mtoia gcvzj fclrn ophuj lbwyq kxucj bpogp bpkmb aptxq tcfaf cfkej jqmhf bnsbw yxdxm ntizj vyhda lzxun epfja hrrul djjlp iuhkk kkbvz yfmuz cbxsm qkzgd sthmm ezfjg pulnv zytbw jaltj vdckg jfrri wmdwh gxrub cvpzq gerxe gzwnp eyndz tamxo bnfrr gehhw yboin gczei ctqmi ahawz kvfck vqama pfasq bazbu dqpzu czhmb eljzl fxmuv cqubj qizyy jayjw qyrfi iqnoe kgepz finku bqmcx ahzsg xdbdi ktsgs uwtku olckw rvqcj grtnh kfbjo potmx pqykz lwgst hoepv ctrjm ywrpj voeel iowpy xzozb hvdrg fwlmr ajfgp orlcg zzdvk eatwt rdpvp bddyt wpone iknrz dwqeh fqvng dsxjc qkoyl cbkfp okybx qovvh tezln kkieb vrpkt ddsnt fruiq hldkv dvfnl bctcq sgwyn kdqdz qkkbk fcjax leemq ljhtt zpeen tnhvr gtlmc wiaeb lfrph laity ysqfo tfxvp nlfjs ftovo aymnd hkccf neidp jctte vpsbn xoyai fnjrt hmppd kkwrf eyhuk hunnp wmqay hnuqk jwlqp ommbp lrnjx ghoph wdpgm jqexv xakpq siswb wwtuc rgcjq fquhy dpioj aclub bsptf phxkk eyqen wnlzh nhnbs qhglq psfay wzzfe oibxh lhrxm ojged gopph qevbs aalff fnagm phrae zlftn mrxnk mmurz rirjm vejlj rcblg wotpe okjvg cqfpq vjgpa fcnjy cafae qpwjw sqxgb xrbfy iqduk ustuf wbrax ogbac snsjo fjwvx cqmpw zyihs gsutl lkxoe anujx kolnh ieoyp ovgvz qmvhj pkugv vujdc cxuzb jgleu tfoyp qjpga fopnu zxewr tsyfv ryqqs gvbwy yysew ftphw idvpq smihd njdce kwqfu fjxmg cvxsq iqhft mlnqy znapn bwbiv yvrtv xnozk qpotj mguzs fjjls wmrgv usrxu brkks smsrx djpzz voxcr ftrsa khrcp oseza tbiny rperb lmwgz guzee xoqax wpsep hklwt oygjo iqhuq hzowt trdlp ubpra nlkwa htvla aoqvz xgkzs fxgjh ikbsk vzfjo slcvg yxmwk gbuli cvkcf mvrip dvuvi yjmqw sxyyp whvkc wkdwx jkffs henhf ulsly xqmhf lypyk xohrb abmbn kmcwt ftebw bzpzs jpqcv vxkti xdetk rvqqj gqazz neeqk scapi fcrbl vwinv jfluv dzqio lmxvt uiltk ycjgp jrjsz qloyj ztcet iztmk psnlm lswgr eubxt nsdfn elohe nlwoi lhavx kjlcb utdgt abnrl hkmjm cywzx jrtkp jeabq zywbv ndbxe khyyj vhufg osqun aogry uovxx cuvxy ophqm qwtuj lvblz rixdc roedo wdaxq jpibf vowwa zttuu hmltt sgyyq bdjan fsvlt vtcxj sobus coqus kgejj seiis dmomb rroxk kffcj fmoqj ziire ukkhh qeisq kgyhc ilrin xirqv drwqh ggrzl urpjy cknqm qxvce murgz bbgoz tsqpj hjvcs atpmv umsqm zdgdo itskl nwafw umitp lzdfc edetu hbqcq nsilf vobdx eafzj cgnap zktvx lzyfk dknss hosst eljut inkhs tczqf kejjt zdtiz dyciv mliee cjwhu pbtgh cuedi amtes kdjfn kiecr ejron wcoxu mbzix rxxyr xmkzr zoney majnq nonzc sihzu thpgx kmpvc fgutd nwjhj ajnmc kvokh rwdkd prjak jxlhu fumls wbglz cwkxd npngh pfivm gvvlx yabav chzek hhssf jotvu qvstv ulvbw smpqh oncwu srbxr smqbd xvjxh dsqkf isaze bdgqo wqruz ovulk bsahd ikbzo ruynh eqiam askjx kwatg yavdn xqooz uwxbj macwv ngqwb vvagx bjvkr jngqf zqvyo dgjaf iobnk rzdgl ausih rfuaf vtnma hrp''')
        self.assertEqual(Enigma1.encrypt_message(message), testOutput)
        ################ Offsets multiple rotors ###############################
        Enigma1.reset()
        Enigma1.set_ring_offset(3, 0)
        Enigma1.set_ring_offset(18, 1)
        Enigma1.set_ring_offset(10, 2)
        testOutput = format(
            '''taaht tkrcw yashk zlmlp jffcq oiuwa kmhfh tgoiq ucjdi tlxrs rmlog oyucw azvbl bmbux nlyyu uxqzk kcfpy vjxji pzebh nvphl dgppp ibqte bqkbr ifnql kbjvc tasxd cfugz hdokd lqjbg jitjt weocw ntryr ugipk spfdt gqshr zassq rjixc ptitc orgrs vyqut peqpn xikpv cvifv lhdux puylv ptjus jsatn qypjk boaob lkgli dcugp ibfpa ldjnw agwpn mevai zxutc amxce cnaye kmumo dzqcx tzytr zxzbv uwudk skxyq krlta yflyf awvbk znzlq qtsba zghkn omsqa tiife zwfte cpzza czczu jwstx bmsxd ifotd zipmd avwpy ohjii ukfwm agbvg ibdep sbmko oyozj qelra elctm ccwor sscci cjjqa vqvpc umsie otzsy nvhag oxbww qjxrj orspq jsqfo snrar xgcor ivkua onrxv hyfsz ytnow bdxqf axdsh pyoqk qjkqi wwvet axjre glnkr iwvor zicky shuaf utnfr iljce opfgv xshyg orxnw yleyl omtbo gmvgr xdatz vrdbg hgkpi gkdfi iepfd quiaw axqdp ifzyb nmggd qoopt uhgna taceg iogdw iwpen osxsa upibe hxxto asrym ufgvb kwgaq ixzrk wnpso sbxob pghfl flzxi errjx rslzc usorv jbnce zwdvl wfeuz zapxe luuse vwhvf uyzyn eomtp yoiwu xxlru islre rsbto ctwyi hbzzd fqiqp pviqb xtiyj nlwdr lkjiv ypphd cpnbk mnvyj rwymi znwuv bqrvv lgoht hdcdh kxwkt izhew oiqrx xgwtj zrqxt kjnnr vhoma sqlkr vlzpe ojvsh vxjjf oizcq vgelv jmkqs saicy kfvcg rhkrb ogwbg fcwcu jimnu axkgp velgy frkgm bkcjb larmn inuro yfqqx mctgg vxznc kjtnl pmihv rlbzj fkffy pumda swxea opkat xxwya htwpk cgqpb iuwqh qmnjz wnmqw clqla vhqpn ulhxy kqttv dwtbc wvtgi zvyxw ivuwx styuh xzfsj dfctb vkflk vlfmd ifdub thxsy jroyz bfqdc vzyjy lpzfx lnphd nskks ovjwq htoay cedcx bxadn jfjjh hlajd ephnk carrh aojyo tajie sfxdf acpyh kajdq vokbb ydmqj undqt ojygf obudu grqjz libam ubwao xkfsx rynuj yhcgg lmwlm cbgpj dwvnt vxidu cvzsd bqwmy hdtzk bklrp mhooj zupag kptyb motjp wwbqm munxn hudnr byzkb pzsvv njdjc xdomh vzjmz zdnxv xugur fifps vybeb qffdm dpxcw ixocy acind dmwpb ixiqa bpjwu nqecn qouob ichxm uazog hsxbk arqxv aijys mygvu fvkdi mmfkr fdezv ceqgy gtwkh pseur awgmr witrk sqjtq dcidv ckdrp bjavy ogkdk rlsfq hdodv cnzod krgdp ezavg sndys bmzyg souuq aywum cogvp nlhka zzrsz awjth hicxs qtaki hqnsy xnved qwhrf vfovj xmcig jgkdr hrauh ipjtt zcvaw eyatv anvwj hedkg ozkfq vtjld jtfxs jrnow odhyi aykrk segvh mncil qpknw nanai ejkzt mvwjy fnzsf hxthc rrxzh yjctd orszi cjedk sbdkq oqebm ineyv ahrpr ozmdt cedph nbtqy kzqqv fpxme irbyz tqjjm fkuac txqen ejsny lpmpm osyxh dqhsx xpopr qgmid oahqd eyjhb bhhvz owmpc qnvln bmmvn rrdhg odnvo fyeel qvxyn efwda wgtvi jyhhx hpsdm gizqw rlepc hzncq slwki cpnqt jajyb ubuwc jemfi kebrn ngnjp lubhy ihtmf qihut uuhne fhtek gowdy bhwqw tlrvn mvjds mzfhx hhnfb wtxed supbn vpokg huawn vndsl gsqvy sxioo qqljj dwryo snpdl subek rwqxy fdkfk zudun ebiyb grwyt lwvop bnjcx jcsmm tompj oqxzk ullkw eyezu mdnzz wpmuk ukbbp tafru zoffn unuid nozyp azcpy hfwkp trxwq vtyxa yhtmd qcifr quryj kboie lcvgw yjvor kmkqq ctruw gbxwd maslw kvwxs oooqb lvaak sgopz jujjy vlvvo wxzwr anzob mjhkp hvgec oqvpi ctnga czzfy yxchz kpyrs wzjae bzmzx tpykh jggyn hppst cmzfh qojne rwtux oscxc puaip hyszw aizbu gzruj jiual cqgmv zfwhm grwzv cazia hpjep hffgv nnbuf nxffk mvmin uwbdr btmda xwkbf bkzve ksgdj rxdvg gcxxi tclzd tsgqh sbapi nubct gmbfb mflmd ftdaa kkbex cfjza yvwfk cxgcy kqdtq yhhqs vkofm vzbkf hejgo qosbt ucyck ridup yvzgl iudxh cjenb jrqhq tbrul xdwie quy''')
        self.assertEqual(Enigma1.encrypt_message(message), testOutput)

    #@uni.skip("Already passed the double step test")
    def test_double_step(self):
        Enigma1 = create_enigma1()
        testoutput = [(chr(a) + 'DQ', chr(a + 1) + 'FS') for a in range(ord('A'), ord('Z'))]
        testoutput.append(('ZDQ', 'AFS'))
        output = []
        for pair in testoutput:
            Enigma1.set_rotors(pair[0])
            Enigma1.rotate_rotors()
            Enigma1.rotate_rotors()
            output.append((pair[0], "".join(
                [Enigma1.rotors[len(Enigma1.rotors) - i].get_top() for i in range(1, len(Enigma1.rotors) + 1)])))
        self.assertEqual(output, testoutput)

    #@uni.skip("Already passed the backwards test")
    def test_backwards(self):
        Enigma1 = create_enigma1()
        ############################## Simple Backspace #########################
        orientation = 'AAA'
        Enigma1.set_rotors(orientation)
        Enigma1.rotate_rotors(forward=False)
        self.assertEqual("".join([Enigma1.rotors[len(Enigma1.rotors) - i].get_top()
                          for i in range(1, len(Enigma1.rotors) + 1)]), 'AAZ')
        ############################## Double Step ##############################
        testoutput = [(chr(a + 1) + 'FS' , chr(a) + 'DQ') for a in range(ord('A'), ord('Z'))]
        testoutput.append(('AFS', 'ZDQ'))
        output = []
        for pair in testoutput:
            Enigma1.set_rotors(pair[0])
            Enigma1.rotate_rotors(forward=False)
            Enigma1.rotate_rotors(forward=False)
            output.append((pair[0], "".join(
                [Enigma1.rotors[len(Enigma1.rotors) - i].get_top() for i in range(1, len(Enigma1.rotors) + 1)])))
        self.assertEqual(output, testoutput)

    #def test_rotors

        

if __name__ == '__main__':
    '''Enigma1 = create_enigma1()
    Enigma1.set_ring_top(13, 0)
    s = str(Enigma1.rotors[0])
    print(s)'''
    uni.main()
    Enigma1 = create_enigma1()
    testouput = [(chr(a), chr(a) + 'DQ') for a in range(ord('A'), ord('Z') + 1)]
    output = []
    print(testouput)
    for pair in testouput:
        Enigma1.set_rotors(pair[1])
        Enigma1.rotate_rotors()
        Enigma1.rotate_rotors()
        output.append((pair[0], "".join([Enigma1.rotors[len(Enigma1.rotors) - i].get_top() for i in range(1, len(Enigma1.rotors) + 1)])))
    print(output, testouput, sep='\n')
