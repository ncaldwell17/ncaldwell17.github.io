import os
import sys
import pandas as pd
import re 

# variables
# header variables
doctype = "<!DOCTYPE html> <html>"
metatitle = "<title>{0}</title>"
head = "<head>"
metadescription = "<meta name='description' content={1}>"
metaphoto = "<meta property='og:image' content='{8}'>"
othermeta = "<meta charset='utf-8'> <meta name='viewport' content='width=device-width, initial-scale=1, shrink-to-fit=no'>"
css = "<link rel='stylesheet' href='template.css'>"
fonts = "<link href='https://fonts.googleapis.com/css?family=Spectral&display=swap' rel='stylesheet'> <link href='https://fonts.googleapis.com/css?family=PT+Sans&display=swap' rel='stylesheet'><link href='https://fonts.googleapis.com/css?family=Acme&display=swap' rel='stylesheet'> <link href='https://fonts.googleapis.com/css?family=Geostar+Fill&display=swap' rel='stylesheet'>"
social = "<link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'>"
js = "<script src='template.js'></script>"
headf = "</head>"

# body variables
body = "<body>"
fader = "<svg id='fader'>"
body_header = "<div class='header'> <a href='/index.html' style='color: white;'><div class='logo'>NCG.com</div></a>"
bheaders = body+fader+body_header

uni_header = "{36}</div>"
main = "<div class='main'>"
body_title = "<div class='title'>{0}</div>"
ssh = uni_header+main+body_title

body_subtitle = "<div class='subtitle'>{1}</div>"
attr_cont = "<div class='attrContainer'> <div class='by'>By <a href='{2}'>{3}</a></div> <div class='email'><a href='{4}'>{5}</a></div> <div class='datetime'>{6} @ {7}</div> </div>"
social_cont = "<div class='socialContainer'> <div class='aSocial'> <i class='fa fa-twitter'></i> </div> <div class='aSocial' style='padding-left: 25px; width: 10px;'> <i class='fa fa-facebook'></i> </div> <div class='aSocial'> <i class='fa fa-reddit'></i> </div> <div class='aSocial'> <i class='fa fa-google'></i> </div> </div>"
containers = body_subtitle+attr_cont+social_cont

body_photo = "<div class='mainPhoto' style='background-image: url({8})'></div>"
caption = "<div class='caption'>{9}</div>"
source = "<div class='source'>{10}</div>"
photoinfo = body_photo+caption+source

first_p = "<p class='something'>{11}</p>"
pz = "<p>{12}</p> <p>{13}</p> <p>{14}</p> <p>{15}</p> <p>{26}</p> <p>{27}</p> <p>{28}</p> <p>{29}</p> <p>{30}</p> <p>{31}</p> <p>{32}</p> <p>{33}</p> <p>{34}</p> <p>{35}</p>"
tag_cont = "<div class='tagContainer'> <div class='aTag'>{16}</div> <div class='aTag'>{17}</div> <div class='aTag'>{18}</div> <div class='aTag' style='margin-right: 0;'>{19}</div> </div>"
readnext = "<div class='readNext'> <div class='secTitle'>Read Next:</div> <li class='aNext'><a href='{20}'>{21}</a></li> <li class='aNext'><a href='{22}'>{23}</a></li> <li class='aNext'><a href='{24}'>{25}</a></li> </div>"
empty = "<div class='empty'></div>\</div>"
writings = first_p+pz+tag_cont+readnext+empty

# footer variables
faderf = "</svg>"
bodyf = "</body>"
htmlf = "</html>"

# meta-variables 
the_head = doctype+metatitle+head+metadescription+metaphoto+othermeta+css+fonts+social+js+headf

the_body = bheaders+ssh+containers+photoinfo+writings

the_footer = faderf+bodyf+htmlf

# helper functions 
def create_post(atype):
    num_in_dir = len([name for name in os.listdir('.')])
    # for some reason, num_in_dir seems to think there's always at least 1 file
    np_idx = (num_in_dir -2) + 1
    str(np_idx)
    blog_loc = "{0}_bp{1}".format(atype, np_idx)
    return blog_loc

def decide_header(atype):
    if atype == 'elections':
        return "<div class='aProject'>Artificial Intelligence</div> <div class='aProject'>Geopolitics</div> <div class='aProject'>Dev. Economics</div> <div class='aProject'>Cybersecurity</div> <div class='aProject'>Issue Analysis</div>"
    if atype == 'ai':
        return "<div class='aProject'>Elections</div> <div class='aProject'>Geopolitics</div> <div class='aProject'>Dev. Economics</div> <div class='aProject'>Cybersecurity</div> <div class='aProject'>Issue Analysis</div>"

def removeO(string):
    new_string = re.sub('Õ',"'",string)
    new_string = re.sub('Ô',"'",new_string)
    new_string = re.sub('Ó','"',new_string)
    new_string = re.sub('Ò','"',new_string)
    return new_string

def normalize(varlist):
    for dataframe in varlist:
        removeO(str(dataframe))
    return varlist

def format_html(varlist, document, header):
    # insert arbitrary variables here
    ablog = document.format(varlist[0], varlist[1], varlist[2], varlist[3], varlist[4], varlist[5], varlist[6],
                            varlist[7], varlist[8], varlist[9], varlist[10], varlist[11], varlist[12], varlist[13],
                            varlist[14], varlist[15], varlist[16], varlist[17], varlist[18], varlist[19], varlist[20],
                            varlist[21], varlist[22], varlist[23], varlist[24], varlist[25], varlist[26], varlist[27],
                            varlist[28], varlist[29], varlist[30], varlist[31], varlist[32], varlist[33], varlist[34],
                            varlist[35], header)
    return ablog


# system arguments

post_type = sys.argv[1]
post_id = int(sys.argv[2])


# debugging
# post_type = 'elections'
# post_id = 1

if __name__ == "__main__":
    document = str(the_head+the_body+the_footer)
    # need a variable holding the dataframe as pd_dataframe
    cd = os.getcwd()
    if post_type == 'elections':
        pd_dataframe = pd.read_csv('templateBlog.csv', index_col=0, encoding = "ISO-8859-1", engine='python', na_filter=False)
    elif post_type == 'ai':
        pd_dataframe = pd.read_csv(cd+"/aiBlog.csv", index_col=0, encoding = "ISO-8859-1", engine='python', na_filter=False)
    # need id 
    id = post_id
    # need a variable creating the list of dataframes 
    df_list = [pd_dataframe['title'][id], pd_dataframe['subtitle'][id], pd_dataframe['aut_href'][id],
               pd_dataframe['author'][id], pd_dataframe['ema_href'][id], pd_dataframe['email'][id],
               pd_dataframe['date'][id], pd_dataframe['time'][id], pd_dataframe['image_path'][id],
               pd_dataframe['caption'][id], pd_dataframe['source'][id],pd_dataframe['one_p'][id], 
               pd_dataframe['two_p'][id], pd_dataframe['three_p'][id], pd_dataframe['four_p'][id],
               pd_dataframe['five_p'][id], pd_dataframe['tag1'][id], pd_dataframe['tag2'][id], 
               pd_dataframe['tag3'][id], pd_dataframe['tag4'][id], pd_dataframe['link_n1'][id],
               pd_dataframe['next1'][id], pd_dataframe['link_n2'][id], pd_dataframe['next2'][id],
               pd_dataframe['link_n3'][id], pd_dataframe['next3'][id], pd_dataframe['extra1'][id],
               pd_dataframe['extra2'][id], pd_dataframe['extra3'][id], pd_dataframe['extra4'][id],
               pd_dataframe['extra5'][id], pd_dataframe['extra6'][id], pd_dataframe['extra7'][id],
               pd_dataframe['extra8'][id], pd_dataframe['extra9'][id], pd_dataframe['extra10'][id]]
    # need a variable holding the normalized list produced from above
    norm_varlist = normalize(df_list)
    # need a method call to produce unique header
    unique_header = decide_header(post_type)
    # formating the new file
    os.chdir("projects/%s/posts/" % post_type)
    bidx = create_post(post_type)
    wf = open("{0}.html".format(bidx), "a")
    aheader = decide_header(post_type)
    # main function

    wf.write(format_html(norm_varlist, document, unique_header))
    wf.close