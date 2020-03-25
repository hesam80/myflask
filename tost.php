<?php session_start() ?>
<html lang="en" Content-Type="text/html" >


<head>
    <meta charset="utf-8">
    <title>PHP Tst</title>
    <style type="text/css" media="all">

.heart
{
    position: relative;
    width: 100px;
    height: 90px;   
    margin: 50px auto;
}

.heart::before,
.heart::after
{
    position: absolute;
    content: "";
    left: 50px;
    top: 0;
    width: 50px;
    height: 80px;
    background: red;
    border-radius: 50px 50px 0 0;
    transform: rotate(-45deg);
    transform-origin: 0 100%;
}
.heart::after
{
    left: 0;
    transform: rotate(45deg);
    transform-origin: 100% 100%;
}
    </style>
	
</head>
<body>

 <div class="box content" id="content">
	<div class="wrap">
		<div class="content-main">
			<div class="content-post">
	           <div class="content-wrap">
		         
		          <h1><a href="https://digwp.com/2011/05/loops/">4 Ways to Loop with WordPress tost</a></h1>
	             
	              <p class="post-author"><em>Posted by Jeff Starr • <span>Updated on</span> <time title="Original Post Date: May 11th, 2011" datetime="2017-02-11T14:30:52+00:00">February 11th, 2017</time></em></p>
	             
	              <img class="featured-image" width="150" height="150" src="img/home-slider/3.jpg" alt="4 Ways to Loop with WordPress">	
	             
	              <div class="heart"></div>
				  <?php 
				  function bekhan($famil){
					  $famil.="حسینی";
					  echo $famil;
				  }
				  $name = "فامیل من";
				  bekhan($name); ?>
				  <div class="heart">
				  <?php   
				      function jam($x){
						  $x+= 2;
						  echo $x;
					  }
					  $y = 3 ;
					  jam($y);
					  
				  ?>
				  </div>
				  
				
</body>
</html>