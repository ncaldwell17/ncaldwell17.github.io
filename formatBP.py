import os
import os.path
import sys
import csv
import pandas as pd
import numpy as np

def create_post(type):
    num_in_dir = len([name for name in os.listdir('.')])
    # for some reason, num_in_dir seems to think there's always at least 1 file
    np_idx = (num_in_dir -2) + 1
    str(np_idx)
    blog_loc = "{0}_bp{1}".format(type, np_idx)
    return blog_loc

def del_if(some_data):
    if pd.isnull(some_data) == True:
        some_data = ''
        return some_data

def format_html(pd_dataframe, id):
    # insert HTML format here
    blog_format = "<!DOCTYPE html> <html> <title>{36}</title> <head> <meta name='description' content='A guide to the positions, fundraising, and predictions on the 2020 General Election.'> <meta property='og:image' content='{8}'><!-- Meta Tags --> <meta charset='utf-8'> <meta name='viewport' content='width=device-width, initial-scale=1, shrink-to-fit=no'> <!-- CSS --> <link rel='stylesheet' href='template.css'> <!-- insert font here --> <link href='https://fonts.googleapis.com/css?family=Spectral&display=swap' rel='stylesheet'> <link href='https://fonts.googleapis.com/css?family=Acme&display=swap' rel='stylesheet'> <link href='https://fonts.googleapis.com/css?family=Geostar+Fill&display=swap' rel='stylesheet'> <!-- Social Media icons --> <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'> <!-- JS --> <script src='template.js'></script> </head> <body> <div class='header'> <div class='logo'>NCG.com</div> <div class='aProject'>Artificial Intelligence</div> <div class='aProject'>Geopolitics</div> <div class='aProject'>Dev. Economics</div> <div class='aProject'>Cybersecurity</div> <div class='aProject'>Issue Analysis</div> </div> <div class='main'> <div class='title'>{0}</div> <div class='subtitle'>{1}</div> <div class='attrContainer'> <div class='by'>By <a href='{2}'>{3}</a></div> <div class='email'><a href='{4}'>{5}</a></div> <div class='datetime'>{6} @ {7}</div> </div> <div class='socialContainer'> <div class='aSocial'> <i class='fa fa-twitter'></i> </div> <div class='aSocial' style='padding-left: 25px; width: 10px;'> <i class='fa fa-facebook'></i> </div> <div class='aSocial'> <i class='fa fa-reddit'></i> </div> <div class='aSocial'> <i class='fa fa-google'></i> </div> </div> <div class='mainPhoto' style='background-image: url({8})'></div> <div class='caption'>{9}</div> <div class='source'>{10}</div> <p class='something'>{11}</p> <p>{12}</p> <p>{13}</p> <p>{14}</p> <p>{15}</p> <p>{26}</p> <p>{27}</p> <p>{28}</p> <p>{29}</p> <p>{30}</p> <p>{31}</p> <p>{32}</p> <p>{33}</p> <p>{34}</p> <p>{35}</p> <div class='tagContainer'> <div class='aTag'>{16}</div> <div class='aTag'>{17}</div> <div class='aTag'>{18}</div> <div class='aTag' style='margin-right: 0;'>{19}</div> </div> <div class='readNext'> <div class='secTitle'>Read Next:</div> <li class='aNext'><a href='{20}'>{21}</a></li> <li class='aNext'><a href='{22}'>{23}</a></li> <li class='aNext'><a href='{24}'>{25}</a></li> </div> <div class='empty'></div>\
         </div> </body> </html>".format(pd_dataframe['title'][id],
                                        pd_dataframe['subtitle'][id],
                                        pd_dataframe['aut_href'][id],
                                        pd_dataframe['author'][id],
                                        pd_dataframe['ema_href'][id],
                                        pd_dataframe['email'][id],
                                        pd_dataframe['date'][id],
                                        pd_dataframe['time'][id],
                                        pd_dataframe['image_path'][id],
                                        pd_dataframe['caption'][id],
                                        pd_dataframe['source'][id],
                                        pd_dataframe['one_p'][id],
                                        pd_dataframe['two_p'][id],
                                        pd_dataframe['three_p'][id],
                                        pd_dataframe['four_p'][id],
                                        pd_dataframe['five_p'][id],
                                        pd_dataframe['tag1'][id],
                                        pd_dataframe['tag2'][id],
                                        pd_dataframe['tag3'][id],
                                        pd_dataframe['tag4'][id],
                                        pd_dataframe['link_n1'][id],
                                        pd_dataframe['next1'][id],
                                        pd_dataframe['link_n2'][id],
                                        pd_dataframe['next2'][id],
                                        pd_dataframe['link_n3'][id],
                                        pd_dataframe['next3'][id],
                                        del_if(pd_dataframe['extra1'][id]),
                                        del_if(pd_dataframe['extra2'][id]),
                                        del_if(pd_dataframe['extra3'][id]),
                                        del_if(pd_dataframe['extra4'][id]),
                                        del_if(pd_dataframe['extra5'][id]),
                                        del_if(pd_dataframe['extra6'][id]),
                                        del_if(pd_dataframe['extra7'][id]),
                                        del_if(pd_dataframe['extra8'][id]),
                                        del_if(pd_dataframe['extra9'][id]),
                                        del_if(pd_dataframe['extra10'][id]),
                                        pd_dataframe['meta_title'][id],
                                        )
    return blog_format
    
post_type = sys.argv[1]
post_id = int(sys.argv[2])

blog_entries = pd.read_csv('templateBlog.csv', index_col=0)

if __name__ == "__main__":
    os.chdir("projects/%s/posts/" % post_type)
    bidx = create_post(post_type)
    wf = open("{0}.html".format(bidx), "a")
    wf.write(format_html(blog_entries, post_id))
    wf.close
