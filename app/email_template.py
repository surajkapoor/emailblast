def email_template():
	return """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
    	<!-- NAME: 1:3 COLUMN - BANDED -->
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>*|MC:SUBJECT|*</title>
        
    <style type="text/css">
		body,#bodyTable,#bodyCell{
			height:100% !important;
			margin:0;
			padding:0;
			width:100% !important;
		}
		table{
			border-collapse:collapse;
		}
		img,a img{
			border:0;
			outline:none;
			text-decoration:none;
		}
		h1,h2,h3,h4,h5,h6{
			margin:0;
			padding:0;
		}
		p{
			margin:1em 0;
			padding:0;
		}
		a{
			word-wrap:break-word;
		}
		.ReadMsgBody{
			width:100%;
		}
		.ExternalClass{
			width:100%;
		}
		.ExternalClass,.ExternalClass p,.ExternalClass span,.ExternalClass font,.ExternalClass td,.ExternalClass div{
			line-height:100%;
		}
		table,td{
			mso-table-lspace:0pt;
			mso-table-rspace:0pt;
		}
		#outlook a{
			padding:0;
		}
		img{
			-ms-interpolation-mode:bicubic;
		}
		body,table,td,p,a,li,blockquote{
			-ms-text-size-adjust:100%;
			-webkit-text-size-adjust:100%;
		}
		#bodyCell{
			padding:0;
		}
		.mcnImage{
			vertical-align:bottom;
		}
		.mcnTextContent img{
			height:auto !important;
		}
	/*
	@tab Page
	@section background style
	@tip Set the background color and top border for your email. You may want to choose colors that match your company's branding.
	*/
		body,#bodyTable{
			/*@editable*/background-color:#ffffff;
		}
	/*
	@tab Page
	@section background style
	@tip Set the background color and top border for your email. You may want to choose colors that match your company's branding.
	*/
		#bodyCell{
			/*@editable*/border-top:0;
		}
	/*
	@tab Page
	@section heading 1
	@tip Set the styling for all first-level headings in your emails. These should be the largest of your headings.
	@style heading 1
	*/
		h1{
			/*@editable*/color:#000000 !important;
			display:block;
			/*@editable*/font-family:Helvetica;
			/*@editable*/font-size:40px;
			/*@editable*/font-style:normal;
			/*@editable*/font-weight:bold;
			/*@editable*/line-height:125%;
			/*@editable*/letter-spacing:-1px;
			margin:0;
			/*@editable*/text-align:left;
		}
	/*
	@tab Page
	@section heading 2
	@tip Set the styling for all second-level headings in your emails.
	@style heading 2
	*/
		h2{
			/*@editable*/color:#030000 !important;
			display:block;
			/*@editable*/font-family:Helvetica;
			/*@editable*/font-size:26px;
			/*@editable*/font-style:normal;
			/*@editable*/font-weight:bold;
			/*@editable*/line-height:125%;
			/*@editable*/letter-spacing:-.75px;
			margin:0;
			/*@editable*/text-align:left;
		}
	/*
	@tab Page
	@section heading 3
	@tip Set the styling for all third-level headings in your emails.
	@style heading 3
	*/
		h3{
			/*@editable*/color:#606060 !important;
			display:block;
			/*@editable*/font-family:Helvetica;
			/*@editable*/font-size:18px;
			/*@editable*/font-style:normal;
			/*@editable*/font-weight:bold;
			/*@editable*/line-height:125%;
			/*@editable*/letter-spacing:-.5px;
			margin:0;
			/*@editable*/text-align:left;
		}
	/*
	@tab Page
	@section heading 4
	@tip Set the styling for all fourth-level headings in your emails. These should be the smallest of your headings.
	@style heading 4
	*/
		h4{
			/*@editable*/color:#808080 !important;
			display:block;
			/*@editable*/font-family:Helvetica;
			/*@editable*/font-size:16px;
			/*@editable*/font-style:normal;
			/*@editable*/font-weight:bold;
			/*@editable*/line-height:125%;
			/*@editable*/letter-spacing:normal;
			margin:0;
			/*@editable*/text-align:left;
		}
	/*
	@tab Preheader
	@section preheader style
	@tip Set the background color and borders for your email's preheader area.
	*/
		#templatePreheader{
			/*@editable*/background-color:#000000;
			/*@editable*/border-top:0;
			/*@editable*/border-bottom:0;
		}
	/*
	@tab Preheader
	@section preheader text
	@tip Set the styling for your email's preheader text. Choose a size and color that is easy to read.
	*/
		.preheaderContainer .mcnTextContent,.preheaderContainer .mcnTextContent p{
			/*@editable*/color:#606060;
			/*@editable*/font-family:Helvetica;
			/*@editable*/font-size:11px;
			/*@editable*/line-height:125%;
			/*@editable*/text-align:left;
		}
	/*
	@tab Preheader
	@section preheader link
	@tip Set the styling for your email's header links. Choose a color that helps them stand out from your text.
	*/
		.preheaderContainer .mcnTextContent a{
			/*@editable*/color:#606060;
			/*@editable*/font-weight:normal;
			/*@editable*/text-decoration:underline;
		}
	/*
	@tab Header
	@section header style
	@tip Set the background color and borders for your email's header area.
	*/
		#templateHeader{
			/*@editable*/background-color:#ffffff;
			/*@editable*/border-top:0;
			/*@editable*/border-bottom:0;
		}
	/*
	@tab Header
	@section header text
	@tip Set the styling for your email's header text. Choose a size and color that is easy to read.
	*/
		.headerContainer .mcnTextContent,.headerContainer .mcnTextContent p{
			/*@editable*/color:#606060;
			/*@editable*/font-family:Helvetica;
			/*@editable*/font-size:15px;
			/*@editable*/line-height:150%;
			/*@editable*/text-align:left;
		}
	/*
	@tab Header
	@section header link
	@tip Set the styling for your email's header links. Choose a color that helps them stand out from your text.
	*/
		.headerContainer .mcnTextContent a{
			/*@editable*/color:#6DC6DD;
			/*@editable*/font-weight:normal;
			/*@editable*/text-decoration:underline;
		}
	/*
	@tab Body
	@section body style
	@tip Set the background color and borders for your email's body area.
	*/
		#templateBody{
			/*@editable*/background-color:#ffffff;
			/*@editable*/border-top:0;
			/*@editable*/border-bottom:0;
		}
	/*
	@tab Body
	@section body text
	@tip Set the styling for your email's body text. Choose a size and color that is easy to read.
	*/
		.bodyContainer .mcnTextContent,.bodyContainer .mcnTextContent p{
			/*@editable*/color:#ffffff;
			/*@editable*/font-family:Helvetica;
			/*@editable*/font-size:15px;
			/*@editable*/line-height:150%;
			/*@editable*/text-align:left;
		}
	/*
	@tab Body
	@section body link
	@tip Set the styling for your email's body links. Choose a color that helps them stand out from your text.
	*/
		.bodyContainer .mcnTextContent a{
			/*@editable*/color:#6DC6DD;
			/*@editable*/font-weight:normal;
			/*@editable*/text-decoration:underline;
		}
	/*
	@tab Columns
	@section column style
	@tip Set the background color and borders for your email's columns area.
	*/
		#templateColumns{
			/*@editable*/background-color:#ffffff;
			/*@editable*/border-top:0;
			/*@editable*/border-bottom:0;
		}
	/*
	@tab Columns
	@section left column text
	@tip Set the styling for your email's left column text. Choose a size and color that is easy to read.
	*/
		.leftColumnContainer .mcnTextContent,.leftColumnContainer .mcnTextContent p{
			/*@editable*/color:#000000;
			/*@editable*/font-family:'Trebuchet MS', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif;
			/*@editable*/font-size:15px;
			/*@editable*/line-height:150%;
			/*@editable*/text-align:left;
		}
	/*
	@tab Columns
	@section left column link
	@tip Set the styling for your email's left column links. Choose a color that helps them stand out from your text.
	*/
		.leftColumnContainer .mcnTextContent a{
			/*@editable*/color:#6DC6DD;
			/*@editable*/font-weight:normal;
			/*@editable*/text-decoration:underline;
		}
	/*
	@tab Columns
	@section center column text
	@tip Set the styling for your email's center column text. Choose a size and color that is easy to read.
	*/
		.centerColumnContainer .mcnTextContent,.centerColumnContainer .mcnTextContent p{
			/*@editable*/color:#606060;
			/*@editable*/font-family:Helvetica;
			/*@editable*/font-size:15px;
			/*@editable*/line-height:150%;
			/*@editable*/text-align:left;
		}
	/*
	@tab Columns
	@section center column link
	@tip Set the styling for your email's center column links. Choose a color that helps them stand out from your text.
	*/
		.centerColumnContainer .mcnTextContent a{
			/*@editable*/color:#6DC6DD;
			/*@editable*/font-weight:normal;
			/*@editable*/text-decoration:underline;
		}
	/*
	@tab Columns
	@section right column text
	@tip Set the styling for your email's right column text. Choose a size and color that is easy to read.
	*/
		.rightColumnContainer .mcnTextContent,.rightColumnContainer .mcnTextContent p{
			/*@editable*/color:#606060;
			/*@editable*/font-family:Helvetica;
			/*@editable*/font-size:15px;
			/*@editable*/line-height:150%;
			/*@editable*/text-align:left;
		}
	/*
	@tab Columns
	@section right column link
	@tip Set the styling for your email's right column links. Choose a color that helps them stand out from your text.
	*/
		.rightColumnContainer .mcnTextContent a{
			/*@editable*/color:#6DC6DD;
			/*@editable*/font-weight:normal;
			/*@editable*/text-decoration:underline;
		}
	/*
	@tab Footer
	@section footer style
	@tip Set the background color and borders for your email's footer area.
	*/
		#templateFooter{
			/*@editable*/background-color:#ffffff;
			/*@editable*/border-top:0;
			/*@editable*/border-bottom:0;
		}
	/*
	@tab Footer
	@section footer text
	@tip Set the styling for your email's footer text. Choose a size and color that is easy to read.
	*/
		.footerContainer .mcnTextContent,.footerContainer .mcnTextContent p{
			/*@editable*/color:#606060;
			/*@editable*/font-family:Helvetica;
			/*@editable*/font-size:11px;
			/*@editable*/line-height:125%;
			/*@editable*/text-align:left;
		}
	/*
	@tab Footer
	@section footer link
	@tip Set the styling for your email's footer links. Choose a color that helps them stand out from your text.
	*/
		.footerContainer .mcnTextContent a{
			/*@editable*/color:#606060;
			/*@editable*/font-weight:normal;
			/*@editable*/text-decoration:underline;
		}
	@media only screen and (max-width: 480px){
		body,table,td,p,a,li,blockquote{
			-webkit-text-size-adjust:none !important;
		}

}	@media only screen and (max-width: 480px){
		body{
			width:100% !important;
			min-width:100% !important;
		}

}	@media only screen and (max-width: 480px){
		table[class=mcnTextContentContainer]{
			width:100% !important;
		}

}	@media only screen and (max-width: 480px){
		table[class=mcnBoxedTextContentContainer]{
			width:100% !important;
		}

}	@media only screen and (max-width: 480px){
		table[class=mcpreview-image-uploader]{
			width:100% !important;
			display:none !important;
		}

}	@media only screen and (max-width: 480px){
		img[class=mcnImage]{
			width:100% !important;
		}

}	@media only screen and (max-width: 480px){
		table[class=mcnImageGroupContentContainer]{
			width:100% !important;
		}

}	@media only screen and (max-width: 480px){
		td[class=mcnImageGroupContent]{
			padding:9px !important;
		}

}	@media only screen and (max-width: 480px){
		td[class=mcnImageGroupBlockInner]{
			padding-bottom:0 !important;
			padding-top:0 !important;
		}

}	@media only screen and (max-width: 480px){
		tbody[class=mcnImageGroupBlockOuter]{
			padding-bottom:9px !important;
			padding-top:9px !important;
		}

}	@media only screen and (max-width: 480px){
		table[class=mcnCaptionTopContent],table[class=mcnCaptionBottomContent]{
			width:100% !important;
		}

}	@media only screen and (max-width: 480px){
		table[class=mcnCaptionLeftTextContentContainer],table[class=mcnCaptionRightTextContentContainer],table[class=mcnCaptionLeftImageContentContainer],table[class=mcnCaptionRightImageContentContainer],table[class=mcnImageCardLeftTextContentContainer],table[class=mcnImageCardRightTextContentContainer]{
			width:100% !important;
		}

}	@media only screen and (max-width: 480px){
		td[class=mcnImageCardLeftImageContent],td[class=mcnImageCardRightImageContent]{
			padding-right:18px !important;
			padding-left:18px !important;
			padding-bottom:0 !important;
		}

}	@media only screen and (max-width: 480px){
		td[class=mcnImageCardBottomImageContent]{
			padding-bottom:9px !important;
		}

}	@media only screen and (max-width: 480px){
		td[class=mcnImageCardTopImageContent]{
			padding-top:18px !important;
		}

}	@media only screen and (max-width: 480px){
		td[class=mcnImageCardLeftImageContent],td[class=mcnImageCardRightImageContent]{
			padding-right:18px !important;
			padding-left:18px !important;
			padding-bottom:0 !important;
		}

}	@media only screen and (max-width: 480px){
		td[class=mcnImageCardBottomImageContent]{
			padding-bottom:9px !important;
		}

}	@media only screen and (max-width: 480px){
		td[class=mcnImageCardTopImageContent]{
			padding-top:18px !important;
		}

}	@media only screen and (max-width: 480px){
		table[class=mcnCaptionLeftContentOuter] td[class=mcnTextContent],table[class=mcnCaptionRightContentOuter] td[class=mcnTextContent]{
			padding-top:9px !important;
		}

}	@media only screen and (max-width: 480px){
		td[class=mcnCaptionBlockInner] table[class=mcnCaptionTopContent]:last-child td[class=mcnTextContent]{
			padding-top:18px !important;
		}

}	@media only screen and (max-width: 480px){
		td[class=mcnBoxedTextContentColumn]{
			padding-left:18px !important;
			padding-right:18px !important;
		}

}	@media only screen and (max-width: 480px){
		td[class=columnsContainer]{
			display:block !important;
			max-width:600px !important;
			width:100% !important;
		}

}	@media only screen and (max-width: 480px){
		td[class=mcnTextContent]{
			padding-right:18px !important;
			padding-left:18px !important;
		}

}	@media only screen and (max-width: 480px){
	/*
	@tab Mobile Styles
	@section template width
	@tip Make the template fluid for portrait or landscape view adaptability. If a fluid layout doesn't work for you, set the width to 300px instead.
	*/
		table[class=templateContainer],table[id=templateColumns],table[class=templateColumn]{
			/*@tab Mobile Styles
@section template width
@tip Make the template fluid for portrait or landscape view adaptability. If a fluid layout doesn't work for you, set the width to 300px instead.*/max-width:600px !important;
			/*@editable*/width:100% !important;
		}

}	@media only screen and (max-width: 480px){
	/*
	@tab Mobile Styles
	@section heading 1
	@tip Make the first-level headings larger in size for better readability on small screens.
	*/
		h1{
			/*@editable*/font-size:24px !important;
			/*@editable*/line-height:125% !important;
		}

}	@media only screen and (max-width: 480px){
	/*
	@tab Mobile Styles
	@section heading 2
	@tip Make the second-level headings larger in size for better readability on small screens.
	*/
		h2{
			/*@editable*/font-size:20px !important;
			/*@editable*/line-height:125% !important;
		}

}	@media only screen and (max-width: 480px){
	/*
	@tab Mobile Styles
	@section heading 3
	@tip Make the third-level headings larger in size for better readability on small screens.
	*/
		h3{
			/*@editable*/font-size:18px !important;
			/*@editable*/line-height:125% !important;
		}

}	@media only screen and (max-width: 480px){
	/*
	@tab Mobile Styles
	@section heading 4
	@tip Make the fourth-level headings larger in size for better readability on small screens.
	*/
		h4{
			/*@editable*/font-size:16px !important;
			/*@editable*/line-height:125% !important;
		}

}	@media only screen and (max-width: 480px){
	/*
	@tab Mobile Styles
	@section Boxed Text
	@tip Make the boxed text larger in size for better readability on small screens. We recommend a font size of at least 16px.
	*/
		table[class=mcnBoxedTextContentContainer] td[class=mcnTextContent],td[class=mcnBoxedTextContentContainer] td[class=mcnTextContent] p{
			/*@editable*/font-size:18px !important;
			/*@editable*/line-height:125% !important;
		}

}	@media only screen and (max-width: 480px){
	/*
	@tab Mobile Styles
	@section Preheader Visibility
	@tip Set the visibility of the email's preheader on small screens. You can hide it to save space.
	*/
		table[id=templatePreheader]{
			/*@editable*/display:block !important;
		}

}	@media only screen and (max-width: 480px){
	/*
	@tab Mobile Styles
	@section Preheader Text
	@tip Make the preheader text larger in size for better readability on small screens.
	*/
		td[class=preheaderContainer] td[class=mcnTextContent],td[class=preheaderContainer] td[class=mcnTextContent] p{
			/*@editable*/font-size:14px !important;
			/*@editable*/line-height:115% !important;
		}

}	@media only screen and (max-width: 480px){
	/*
	@tab Mobile Styles
	@section Header Text
	@tip Make the header text larger in size for better readability on small screens.
	*/
		td[class=headerContainer] td[class=mcnTextContent],td[class=headerContainer] td[class=mcnTextContent] p{
			/*@editable*/font-size:18px !important;
			/*@editable*/line-height:125% !important;
		}

}	@media only screen and (max-width: 480px){
	/*
	@tab Mobile Styles
	@section Body Text
	@tip Make the body text larger in size for better readability on small screens. We recommend a font size of at least 16px.
	*/
		td[class=bodyContainer] td[class=mcnTextContent],td[class=bodyContainer] td[class=mcnTextContent] p{
			/*@editable*/font-size:18px !important;
			/*@editable*/line-height:125% !important;
		}

}	@media only screen and (max-width: 480px){
	/*
	@tab Mobile Styles
	@section Left Column Text
	@tip Make the left column text larger in size for better readability on small screens. We recommend a font size of at least 16px.
	*/
		td[class=leftColumnContainer] td[class=mcnTextContent],td[class=leftColumnContainer] td[class=mcnTextContent] p{
			/*@editable*/font-size:18px !important;
			/*@editable*/line-height:125% !important;
		}

}	@media only screen and (max-width: 480px){
	/*
	@tab Mobile Styles
	@section Center Column Text
	@tip Make the center column text larger in size for better readability on small screens. We recommend a font size of at least 16px.
	*/
		td[class=centerColumnContainer] td[class=mcnTextContent],td[class=centerColumnContainer] td[class=mcnTextContent] p{
			/*@editable*/font-size:18px !important;
			/*@editable*/line-height:125% !important;
		}

}	@media only screen and (max-width: 480px){
	/*
	@tab Mobile Styles
	@section Right Column Text
	@tip Make the right column text larger in size for better readability on small screens. We recommend a font size of at least 16px.
	*/
		td[class=rightColumnContainer] td[class=mcnTextContent],td[class=rightColumnContainer] td[class=mcnTextContent] p{
			/*@editable*/font-size:18px !important;
			/*@editable*/line-height:125% !important;
		}

}	@media only screen and (max-width: 480px){
	/*
	@tab Mobile Styles
	@section footer text
	@tip Make the body content text larger in size for better readability on small screens.
	*/
		td[class=footerContainer] td[class=mcnTextContent],td[class=footerContainer] td[class=mcnTextContent] p{
			/*@editable*/font-size:14px !important;
			/*@editable*/line-height:115% !important;
		}

}	@media only screen and (max-width: 480px){
		td[class=footerContainer] a[class=utilityLink]{
			display:block !important;
		}

}</style></head>"""

def email_template2(first_name, recommendations):
	return """<body leftmargin="0" marginwidth="0" topmargin="0" marginheight="0" offset="0">
        <center>
            <table align="center" border="0" cellpadding="0" cellspacing="0" height="100%" width="100%" id="bodyTable">
                <tr>
                    <td align="center" valign="top" id="bodyCell">
                        <!-- BEGIN TEMPLATE // -->
                        <table border="0" cellpadding="0" cellspacing="0" width="100%">
                            <tr>
                                <td align="center" valign="top">
                                    <!-- BEGIN PREHEADER // -->
                                    <table border="0" cellpadding="0" cellspacing="0" width="100%" id="templatePreheader">
                                        <tr>
                                        	<td align="center" valign="top">
                                                <table border="0" cellpadding="0" cellspacing="0" width="600" class="templateContainer">
                                                    <tr>
                                                        <td valign="top" class="preheaderContainer" style="padding-top:9px;"></td>
                                                    </tr>
                                                </table>
                                            </td>                                            
                                        </tr>
                                    </table>
                                    <!-- // END PREHEADER -->
                                </td>
                            </tr>
                            <tr>
                                <td align="center" valign="top">
                                    <!-- BEGIN HEADER // -->
                                    <table border="0" cellpadding="0" cellspacing="0" width="100%" id="templateHeader">
                                        <tr>
                                            <td align="center" valign="top">
                                                <table border="0" cellpadding="0" cellspacing="0" width="600" class="templateContainer">
                                                    <tr>
                                                        <td valign="top" class="headerContainer" style="padding-top:10px; padding-bottom:10px;"><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnCaptionBlock">
    <tbody class="mcnCaptionBlockOuter">
        <tr>
            <td class="mcnCaptionBlockInner" valign="top" style="padding:9px;">
                



<table border="0" cellpadding="0" cellspacing="0" class="mcnCaptionRightContentOuter" width="100%">
    <tbody><tr>
        <td valign="top" class="mcnCaptionRightContentInner" style="padding:0 9px ;">
            <table align="left" border="0" cellpadding="0" cellspacing="0" class="mcnCaptionRightImageContentContainer">
                <tbody><tr>
                    <td class="mcnCaptionRightImageContent" valign="top">
                    
                        

                        <img alt="" src="https://gallery.mailchimp.com/150b63e56424afcb3b923306b/images/19de6a14-1992-4396-823f-4e30d9c1636d.png" width="264" style="max-width:1200px;" class="mcnImage">
                        

                    
                    </td>
                </tr>
            </tbody></table>
            <table class="mcnCaptionRightTextContentContainer" align="right" border="0" cellpadding="0" cellspacing="0" width="264">
                <tbody><tr>
                    <td valign="top" class="mcnTextContent">
                        <div style="text-align: center;"><br>
<br>
<span style="color:#000000"><span style="font-size:11px"><span style="font-size:14px"><strong>OrderGroove Outdoor Terrace<br>
75 Broad Street, 23rd Floor, New York, NY. 100014</strong></span><br>
<br>
Tech &amp; Design: 5:00&nbsp;- 6:30<br>
Business: 6:30 -&nbsp;8:00</span></span></div>

                    </td>
                </tr>
            </tbody></table>
        </td>
    </tr>
</tbody></table>




            </td>
        </tr>
    </tbody>
</table></td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                    </table>
                                    <!-- // END HEADER -->
                                </td>
                            </tr>
                            <tr>
                                <td align="center" valign="top">
                                    <!-- BEGIN BODY // -->
                                    <table border="0" cellpadding="0" cellspacing="0" width="100%" id="templateBody">
                                        <tr>
                                            <td align="center" valign="top">
                                                <table border="0" cellpadding="0" cellspacing="0" width="600" class="templateContainer">
                                                    <tr>
                                                        <td valign="top" class="bodyContainer" style="padding-top:10px; padding-bottom:10px;"><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock">
    <tbody class="mcnTextBlockOuter">
        <tr>
            <td valign="top" class="mcnTextBlockInner">
                
                <table align="left" border="0" cellpadding="0" cellspacing="0" width="600" class="mcnTextContentContainer">
                    <tbody><tr>
                        
                        <td valign="top" class="mcnTextContent" style="padding: 9px 18px;color: #000000;font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;font-size: 12px;">
                        
                            <div style="text-align: center;">
<div style="text-align: left;">
<hr></div>

<div style="text-align: center;"><br>
<span style="font-size:14px">Hi {first_name},&nbsp;</span><br>
&nbsp;</div>

<div style="text-align: center;"><span style="font-size:14px"><span style="background-color:#FFFFFF"><strong>Not sure who to talk to tonight? </strong><br>
<br>
Based on the roles you expressed&nbsp;interested in, we've recommended some people from our companies especially for you...</span></span></div>
<br>
&nbsp;</div>

                        </td>
                    </tr>
                </tbody></table>
                
            </td>
        </tr>
    </tbody>
</table></td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                    </table>
                                    <!-- // END BODY -->
                                </td>
                            </tr>
                            <tr>
                                <td align="center" valign="top">
                                    <!-- BEGIN COLUMNS // -->
                                    <table border="0" cellpadding="0" cellspacing="0" width="100%" id="templateColumns">
                                        <tr>
                                            <td align="center" valign="top">
                                                <table border="0" cellpadding="0" cellspacing="0" width="600" class="templateContainer">
                                                    <tr>
                                                        <td align="left" valign="top" class="columnsContainer" width="33%">
                                                            <table border="0" cellpadding="0" cellspacing="0" width="100%" class="templateColumn">
                                                                <tr>
                                                                    <td valign="top" class="leftColumnContainer"><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnCaptionBlock">
    <tbody class="mcnCaptionBlockOuter">
        <tr>
            <td class="mcnCaptionBlockInner" valign="top" style="padding:9px;">
                

<table align="left" border="0" cellpadding="0" cellspacing="0" class="mcnCaptionBottomContent" width="false">
    <tbody><tr>
        <td class="mcnCaptionBottomImageContent" align="center" valign="top" style="padding:0 9px 9px 9px;">
        
            
            <a href={recommendation_1[2]} title="" class="" target="_blank">
            

            <img alt={recommendation_1[1]} src={recommendation_1[3]} width="100" style="max-width:100px;" class="mcnImage">
            </a>
        
        </td>
    </tr>
    <tr>
        <td class="mcnTextContent" valign="top" style="padding: 0px 9px;color: #000000;font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;font-size: 11px;font-style: normal;line-height: 100%;text-align: center;" width="164">
            <div style="text-align: center;"><span style="font-size:11px">From {recommendation_1[0]}:<br>
<br>
<br>
{recommendation_1[1]}<br>
<strong>{recommendation_1[4]}</strong></span><br>
<br>
<br>
<em>Hiring for<br>
{recommendation_1[5]}<br>
jobs</em><br>
<br>
&nbsp;</div>

<div style="text-align: center;"><span style="font-size:11px"><em><a href={recommendation_1[2]} target="_blank">View&nbsp;My&nbsp;LinkedIn</a></em></span><br>
-----<br>
&nbsp;</div>

        </td>
    </tr>
</tbody></table>





            </td>
        </tr>
    </tbody>
</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnCaptionBlock">
    <tbody class="mcnCaptionBlockOuter">
        <tr>
            <td class="mcnCaptionBlockInner" valign="top" style="padding:9px;">
                

<table align="left" border="0" cellpadding="0" cellspacing="0" class="mcnCaptionBottomContent" width="false">
    <tbody><tr>
        <td class="mcnCaptionBottomImageContent" align="center" valign="top" style="padding:0 9px 9px 9px;">
        
            
            <a href={recommendation_2[2]} title="" class="" target="_blank">
            

            <img alt={recommendation_2[1]} src={recommendation_2[3]} width="100" style="max-width:100px;" class="mcnImage">
            </a>
        
        </td>
    </tr>
    <tr>
        <td class="mcnTextContent" valign="top" style="padding: 0px 9px;color: #000000;font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;font-size: 11px;font-style: normal;line-height: 100%;text-align: center;" width="164">
            <div style="text-align: center;"><span style="font-size:11px">From {recommendation_2[0]}:</em><br>
<br>
<br>
{recommendation_2[1]}<br>
<strong>{recommendation_2[4]}</strong><br>
<br>
<br>
<em>Hiring for<br>
{recommendation_2[5]}<br>
jobs</em></span><br>
<br>
&nbsp;</div>

<div style="text-align: center;"><span style="font-size:11px"><em><a href={recommendation_2[2]} target="_blank">View&nbsp;My&nbsp;LinkedIn</a><br>
-----</em></span></div>

        </td>
    </tr>
</tbody></table>





            </td>
        </tr>
    </tbody>
</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnCaptionBlock">
    <tbody class="mcnCaptionBlockOuter">
        <tr>
            <td class="mcnCaptionBlockInner" valign="top" style="padding:9px;">
                

<table align="left" border="0" cellpadding="0" cellspacing="0" class="mcnCaptionBottomContent" width="false">
    <tbody><tr>
        <td class="mcnCaptionBottomImageContent" align="center" valign="top" style="padding:0 9px 9px 9px;">
        
            
            <a href={recommendation_3[2]} title="" class="" target="_blank">
            

            <img alt={recommendation_3[1]} src={recommendation_3[3]} width="100" style="max-width:100px;" class="mcnImage">
            </a>
        
        </td>
    </tr>
    <tr>
        <td class="mcnTextContent" valign="top" style="padding: 0px 9px;color: #000000;font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;font-size: 11px;font-style: normal;line-height: 100%;text-align: center;" width="164">
            <div style="text-align: center;"><span style="font-size:11px">From {recommendation_3[0]}:<br>
<br>
<br>
{recommendation_3[1]}:<br>
<strong>{recommendation_3[4]}</strong><br>
<br>
<br>
<em>Hiring for<br>
{recommendation_3[5]}<br>
jobs</em></span><br>
<br>
&nbsp;</div>

<div style="text-align: center;"><span style="font-size:11px"><em><a href={recommendation_3[2]}: target="_blank">View&nbsp;My&nbsp;LinkedIn</a><br>
-----</em></span></div>

        </td>
    </tr>
</tbody></table>





            </td>
        </tr>
    </tbody>
</table></td>
                                                                </tr>
                                                            </table>
                                                        </td>
                                                        <td align="left" valign="top" class="columnsContainer" width="33%">
                                                            <table border="0" cellpadding="0" cellspacing="0" width="100%" class="templateColumn">
                                                                <tr>
                                                                    <td valign="top" class="centerColumnContainer"><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnCaptionBlock">
    <tbody class="mcnCaptionBlockOuter">
        <tr>
            <td class="mcnCaptionBlockInner" valign="top" style="padding:9px;">
                

<table align="left" border="0" cellpadding="0" cellspacing="0" class="mcnCaptionBottomContent" width="false">
    <tbody><tr>
        <td class="mcnCaptionBottomImageContent" align="center" valign="top" style="padding:0 9px 9px 9px;">
        
            
            <a href={recommendation_4[2]} title="" class="" target="_blank">
            

            <img alt={recommendation_4[1]} src={recommendation_4[3]} width="100" style="max-width:100px;" class="mcnImage">
            </a>
        
        </td>
    </tr>
    <tr>
        <td class="mcnTextContent" valign="top" style="padding: 0px 9px;color: #000000;font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;font-size: 11px;font-style: normal;line-height: 100%;text-align: center;" width="164">
            <div style="text-align: center;"><span style="font-size:11px">From {recommendation_4[0]}:<br>
<br>
<br>
{recommendation_4[1]}<br>
<strong>{recommendation_4[4]}</strong><br>
<br>
<br>
<em>Hiring for<br>
{recommendation_4[5]}</em></span><br>
jobs<br>
<br>
&nbsp;</div>

<div style="text-align: center;"><span style="font-size:11px"><em><a href={recommendation_4[2]} target="_blank">View&nbsp;My&nbsp;LinkedIn</a><br>
-----</em></span></div>

<div style="text-align: center;">&nbsp;</div>

        </td>
    </tr>
</tbody></table>





            </td>
        </tr>
    </tbody>
</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnCaptionBlock">
    <tbody class="mcnCaptionBlockOuter">
        <tr>
            <td class="mcnCaptionBlockInner" valign="top" style="padding:9px;">
                

<table align="left" border="0" cellpadding="0" cellspacing="0" class="mcnCaptionBottomContent" width="false">
    <tbody><tr>
        <td class="mcnCaptionBottomImageContent" align="center" valign="top" style="padding:0 9px 9px 9px;">
        
            
            <a href={recommendation_5[2]} title="" class="" target="_blank">
            

            <img alt={recommendation_5[2]} src={recommendation_5[3]} width="100" style="max-width:100px;" class="mcnImage">
            </a>
        
        </td>
    </tr>
    <tr>
        <td class="mcnTextContent" valign="top" style="padding: 0px 9px;color: #000000;font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;font-size: 11px;font-style: normal;line-height: 100%;text-align: center;" width="164">
            <div style="text-align: center;"><span style="font-size:11px">From {recommendation_5[0]}:<br>
<br>
<br>
{recommendation_5[1]}<br>
<strong>{recommendation_5[4]}</strong><br>
<br>
<br>
<em>Hiring for<br>
{recommendation_5[5]}<br>
jobs</em></span><br>
<br>
&nbsp;</div>

<div style="text-align: center;"><span style="font-size:11px"><em><a href={recommendation_5[2]} target="_blank">View&nbsp;My&nbsp;LinkedIn</a></em></span><br>
<span style="font-size:11px"><em>-----</em></span></div>

        </td>
    </tr>
</tbody></table>





            </td>
        </tr>
    </tbody>
</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnCaptionBlock">
    <tbody class="mcnCaptionBlockOuter">
        <tr>
            <td class="mcnCaptionBlockInner" valign="top" style="padding:9px;">
                

<table align="left" border="0" cellpadding="0" cellspacing="0" class="mcnCaptionBottomContent" width="false">
    <tbody><tr>
        <td class="mcnCaptionBottomImageContent" align="center" valign="top" style="padding:0 9px 9px 9px;">
        
            
            <a href={recommendation_6[2]} title="" class="" target="_blank">
            

            <img alt={recommendation_6[1]} src={recommendation_6[3]} width="100" style="max-width:100px;" class="mcnImage">
            </a>
        
        </td>
    </tr>
    <tr>
        <td class="mcnTextContent" valign="top" style="padding: 0px 9px;color: #000000;font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;font-size: 11px;font-style: normal;line-height: 100%;text-align: center;" width="164">
            <div style="text-align: center;"><span style="font-size:11px">From {recommendation_6[0]}:<br>
<br>
<br>
{recommendation_6[1]}<br>
<strong>{recommendation_6[4]}</strong><br>
<br>
<br>
<em>Hiring for<br>
{recommendation_6[5]}<br>
jobs</em></span><br>
<br>
&nbsp;</div>

<div style="text-align: center;"><span style="font-size:11px"><em><a href={recommendation_6[2]} target="_blank">View&nbsp;My&nbsp;LinkedIn</a><br>
-----</em></span></div>

        </td>
    </tr>
</tbody></table>





            </td>
        </tr>
    </tbody>
</table></td>
                                                                </tr>
                                                            </table>
                                                        </td>
                                                        <td align="left" valign="top" class="columnsContainer" width="33%">
                                                            <table border="0" cellpadding="0" cellspacing="0" width="100%" class="templateColumn">
                                                                <tr>
                                                                    <td valign="top" class="rightColumnContainer"><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnCaptionBlock">
    <tbody class="mcnCaptionBlockOuter">
        <tr>
            <td class="mcnCaptionBlockInner" valign="top" style="padding:9px;">
                

<table align="left" border="0" cellpadding="0" cellspacing="0" class="mcnCaptionBottomContent" width="false">
    <tbody><tr>
        <td class="mcnCaptionBottomImageContent" align="center" valign="top" style="padding:0 9px 9px 9px;">
        
            
            <a href={recommendation_7[2]} title="" class="" target="_blank">
            

            <img alt={recommendation_7[1]} src={recommendation_7[3]} width="100" style="max-width:100px;" class="mcnImage">
            </a>
        
        </td>
    </tr>
    <tr>
        <td class="mcnTextContent" valign="top" style="padding: 0px 9px;color: #000000;font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;font-size: 11px;font-style: normal;line-height: 100%;text-align: center;" width="164">
            <div style="text-align: center;"><span style="font-size:11px">From {recommendation_7[0]}:<br>
<br>
<br>
{recommendation_7[1]}<br>
<strong>{recommendation_7[4]}</strong><br>
<br>
<br>
<em>Hiring for<br>
{recommendation_7[5]}<br>
jobs</em></span><br>
&nbsp;</div>
&nbsp;

<div style="text-align: center;"><span style="font-size:11px"><em><a href={recommendation_7[2]} target="_blank">View&nbsp;My&nbsp;LinkedIn</a></em></span><br>
-----<br>
&nbsp;</div>

        </td>
    </tr>
</tbody></table>





            </td>
        </tr>
    </tbody>
</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnCaptionBlock">
    <tbody class="mcnCaptionBlockOuter">
        <tr>
            <td class="mcnCaptionBlockInner" valign="top" style="padding:9px;">
                

<table align="left" border="0" cellpadding="0" cellspacing="0" class="mcnCaptionBottomContent" width="false">
    <tbody><tr>
        <td class="mcnCaptionBottomImageContent" align="center" valign="top" style="padding:0 9px 9px 9px;">
        
            
            <a href={recommendation_8[2]} title="" class="" target="_blank">
            

            <img alt={recommendation_8[1]} src={recommendation_8[3]} width="100" style="max-width:100px;" class="mcnImage">
            </a>
        
        </td>
    </tr>
    <tr>
        <td class="mcnTextContent" valign="top" style="padding: 0px 9px;color: #000000;font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;font-size: 11px;font-style: normal;line-height: 100%;text-align: center;" width="164">
            <div style="text-align: center;"><span style="font-size:11px">From {recommendation_8[0]}:<br>
<br>
<br>
{recommendation_8[1]}</span><br>
<strong>{recommendation_8[4]}</strong><br>
<br>
<em>Hiring for<br>
{recommendation_8[5]}<br>
jobs</em></span><br>
<br>
&nbsp;</div>

<div style="text-align: center;"><span style="font-size:11px"><em><a href={recommendation_8[2]} target="_blank">View&nbsp;My&nbsp;LinkedIn</a><br>
-----</em></span></div>

        </td>
    </tr>
</tbody></table>





            </td>
        </tr>
    </tbody>
</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnCaptionBlock">
    <tbody class="mcnCaptionBlockOuter">
        <tr>
            <td class="mcnCaptionBlockInner" valign="top" style="padding:9px;">
                

<table align="left" border="0" cellpadding="0" cellspacing="0" class="mcnCaptionBottomContent" width="false">
    <tbody><tr>
        <td class="mcnCaptionBottomImageContent" align="center" valign="top" style="padding:0 9px 9px 9px;">
        
            
            <a href={recommendation_9[2]} title="" class="" target="_blank">
            

            <img alt={recommendation_9[1]} src={recommendation_9[3]} width="100" style="max-width:100px;" class="mcnImage">
            </a>
        
        </td>
    </tr>
    <tr>
        <td class="mcnTextContent" valign="top" style="padding: 0px 9px;color: #000000;font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;font-size: 11px;font-style: normal;line-height: 100%;text-align: center;" width="164">
            <div style="text-align: center;">From {recommendation_9[0]}:<br>
<br>
<br>
{recommendation_9[1]}<br>
<strong>{recommendation_9[4]}</strong><br>
<br>
<br>
<em>Hiring for<br>
{recommendation_9[5]}<br>
jobs</em><br>
<br>
&nbsp;</div>

<div style="text-align: center;"><span style="font-size:11px"><em><a href={recommendation_9[2]} target="_blank">View&nbsp;My&nbsp;LinkedIn</a><br>
-----</em></span></div>

        </td>
    </tr>
</tbody></table>





            </td>
        </tr>
    </tbody>
</table></td>
                                                                </tr>
                                                            </table>
                                                        </td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                    </table>
                                    <!-- // END COLUMNS -->
                                </td>
                            </tr>
                            <tr>
                                <td align="center" valign="top">
                                    <!-- BEGIN FOOTER // -->
                                    <table border="0" cellpadding="0" cellspacing="0" width="100%" id="templateFooter">
                                        <tr>
                                            <td align="center" valign="top">
                                                <table border="0" cellpadding="0" cellspacing="0" width="600" class="templateContainer">
                                                    <tr>
                                                        <td valign="top" class="footerContainer" style="padding-top:10px; padding-bottom:10px;"><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnButtonBlock">
    <tbody class="mcnButtonBlockOuter">
        <tr>
            <td style="padding-top:0; padding-right:18px; padding-bottom:18px; padding-left:18px;" valign="top" align="center" class="mcnButtonBlockInner">
                <table border="0" cellpadding="0" cellspacing="0" class="mcnButtonContentContainer" style="border-collapse: separate !important;border: 2px solid #000000;border-top-left-radius: 5px;border-top-right-radius: 5px;border-bottom-right-radius: 5px;border-bottom-left-radius: 5px;background-color: #BBEBDD;">
                    <tbody>
                        <tr>
                            <td align="center" valign="middle" class="mcnButtonContent" style="font-family: Arial; font-size: 16px; padding: 16px;">
                                <a class="mcnButton " title="COMPANY PROFILES" href="http://" target="_blank" style="font-weight: bold;letter-spacing: normal;line-height: 100%;text-align: center;text-decoration: none;color: #000000;">COMPANY PROFILES</a>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </td>
        </tr>
    </tbody>
</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock">
    <tbody class="mcnTextBlockOuter">
        <tr>
            <td valign="top" class="mcnTextBlockInner">
                
                <table align="left" border="0" cellpadding="0" cellspacing="0" width="600" class="mcnTextContentContainer">
                    <tbody><tr>
                        
                        <td valign="top" class="mcnTextContent" style="padding: 9px 18px;color: #FFFFFF;">
                        
                            <div style="text-align: center;"><span style="color:#000000"><span style="line-height:20.7999992370605px">Can't make it? Check out the&nbsp;TalentHack Company board and email or LinkedIn message anyone you are interested in working for. They want to hear from you!</span></span></div>

                        </td>
                    </tr>
                </tbody></table>
                
            </td>
        </tr>
    </tbody>
</table></td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                    </table>
                                    <!-- // END FOOTER -->
                                </td>
                            </tr>
                        </table>
                        <!-- // END TEMPLATE -->
                    </td>
                </tr>
            </table>
        </center>
    </body>
</html>
	""".format(first_name=first_name, **recommendations)