import re

html = """
<div class="thumb">
<a href="/article/120555322" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/12055/120555322/medium/app120555322.jpeg" alt="糗事#120555322" class="illustration" width="100%" height="auto">
</a>
</div>


<div class="article block untagged mb15 typs_recent" id="qiushi_tag_120554347">


<div class="author clearfix">
<a href="/users/7961263/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/796/7961263/thumb/2016083010263956.JPEG?imageView2/1/w/90/h/90" alt="凯德无">
</a>
<a href="/users/7961263/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
凯德无
</h2>
</a>
<div class="articleGender manIcon">48</div>
</div>

<a href="/article/120554347" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


说什么呢？敬业精神还是值得提倡的。教室突然停电了，老师只能用手机上的电筒继续讲课！这天还那么热，风扇也是摆设！正能量还是要传播一下！（白天，可是教室采光不好，如同夜晚）

</span>

</div>
</a>
<!-- 图片或gif -->



<div class="thumb">

<a href="/article/120554347" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/12055/120554347/medium/app120554347.jpeg" alt="糗事#120554347" class="illustration" width="100%" height="auto">
</a>
</div>


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">264</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/120554347" data-share="/article/120554347" id="c-120554347" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">3</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_120554347" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-120554347" class="up">
<a href="javascript:voting(120554347,1)" class="voting" data-article="120554347" id="up-120554347" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">269</span>
</a>
</li>
<li id="vote-dn-120554347" class="down">
<a href="javascript:voting(120554347,-1)" class="voting" data-article="120554347" id="dn-120554347" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-5</span>
</a>
</li>
<li class="comments">
<a href="/article/120554347" id="c-120554347" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>



<div class="article block untagged mb15 typs_hot" id="qiushi_tag_120554002">


<div class="author clearfix">
<a href="/users/16749385/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/1674/16749385/thumb/2016101709394951.JPEG?imageView2/1/w/90/h/90" alt="王八与蛋">
</a>
<a href="/users/16749385/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
王八与蛋
</h2>
</a>
<div class="articleGender manIcon">99</div>
</div>

<a href="/article/120554002" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>
记得小学的时候，住校的大妈级师娘绕着校园大骂：“哪个小混蛋？每次都偷我的内裤！劳动大扫除不会自己带抹布啊？”
</span>
</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->
<span class="stats-vote"><i class="number">3421</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/120554002" data-share="/article/120554002" id="c-120554002" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">16</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_120554002" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-120554002" class="up">
<a href="javascript:voting(120554002,1)" class="voting" data-article="120554002" id="up-120554002" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">3438</span>
</a>
</li>
<li id="vote-dn-120554002" class="down">
<a href="javascript:voting(120554002,-1)" class="voting" data-article="120554002" id="dn-120554002" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-17</span>
</a>
</li>
<li class="comments">
<a href="/article/120554002" id="c-120554002" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

<a href="/article/120554002" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>

<span class="cmt-name">污妖王毒鸡汤：</span>
<div class="main-text">
楼猪每当想起这一幕，就又把飞机痛打一顿，以纪念自己的青葱岁月。[如花]
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


55

</div>
</div>
</div>
</a>

</div>


"""
# \d+?
# <div class="thumb">
# <a href="/article/120554347" target="_blank">
# <img src="//pic.qiushibaike.com/system/pictures/12055/120554347/medium/app120554347.jpeg" alt="糗事#120554347" class="illustration" width="100%" height="auto">
# </a>
# </div>
#
# <div class="article block untagged mb15 typs_recent" id="qiushi_tag_120554347">
# <div class="author clearfix">
# <a href="/users/7961263/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">
#
# <img src="//pic.qiushibaike.com/system/avtnew/796/7961263/thumb/2016083010263956.JPEG?imageView2/1/w/90/h/90" alt="凯德无">
# </a>
# <a href="/users/7961263/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
# <h2>
# 凯德无
# </h2>
# </a>
# <div class="articleGender manIcon">48</div>
# </div>

# imgs = re.findall(r'<div class="thumb">.*?<img src="(.*?)" alt=".*?"', html, flags=re.S)

imgs = re.findall(r'<img src="(.*?)"', html,)

# imgs = re.findall(r'//pic.qiushibaike.com/system/pictures/\d+/\d+/medium/app\d+.jpeg', html)

for img in imgs:
    print(img)




















