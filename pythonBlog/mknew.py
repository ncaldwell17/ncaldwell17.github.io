import os
import sys

# variables
js_content = "function fadeInPage() { \
                if (!window.AnimationEvent) { return; } \
                var fader = document.getElementById('fader'); \
                fader.classList.add('fade-out'); \
            }"

html_header = "<!DOCTYPE html> \
                <html> \
                \
                <title>Interactive Resume</title> \
                \
                <head> \
                    <!-- Meta Tags  --> \
                        <meta charset='utf-8'> \
                        <meta name='viewport' content='width=device-width, initial-scale=1, shrink-to-fit=no'> \
                        <meta property='og:title' content='{0}'> \
                        <meta property='og:description' content='I'm a machine learning engineer focused on designing visualizations for statistical analysis of big data.'> \
                        <meta property='og:image' content='{10}'> \
                        <meta property='og:url' content='ncaldwellgatsos.com/iResume.html'> \
                    <!-- CSS --> \
                        <link rel='stylesheet' href='iResume.css'> \
                        <!-- insert font here --> \
                        <link href='https://fonts.googleapis.com/css?family=Spectral&display=swap' rel='stylesheet'> \
                        <link href='https://fonts.googleapis.com/css?family=Diplomata&display=swap' rel='stylesheet'> \
                        <!-- insert js/css objects here --> \
                        <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'> \
                    <!-- JS --> \
                        <script type='text/JavaScript' src='http://ajax.googleapis.com/ajax/libs/jquery/1.10.1/jquery.min.js'></script> \
                        <script src='iResume.js'></script> \
                </head>"

html_body = "\n \
             \n \
             <body> \n \
                 <svg id='fader'> \n \
             \n \
             \n \
                </svg> \n \
             \n"

html_js = "<script> \
                fadeInPage(); \
                            \
                //fade-in, fade-out \
                document.addEventListener('DOMContentLoaded', function() { \
                    if (!window.AnimationEvent) { return; } \
                    var anchors = document.getElementsByTagName('a'); \
                                    \
                for (var idx=0; idx<anchors.length; idx+=1) { \
                    if (anchors[idx].hostname !== window.location.hostname) { \
                    continue; \
                    } \
                anchors[idx].addEventListener('click', function(event) { \
                var localPath = '/wp-content/uploads/' \
                                    \
                if (anchors[idx].hostname !== window.location.hostname || anchors[idx].pathname === window.location.pathname || anchors[idx].pathname.indexOf(localPath) !== -1) { \
                //continue; \
                } \
                var fader = document.getElementById('fader'), \
                    anchor = event.currentTarget; \
                                    \
                var listener = function() { \
                    window.location = anchor.href; \
                    fader.removeEventListener('animationend', listener); \
                }; \
                fader.addEventListener('animationend', listener); \
                                    \
                event.preventDefault(); \
                fader.classList.add('fade-in'); \
                }); \
                } \
                }); \
                window.addEventListener('pageshow', function (event) { \
                if (!event.persisted) { \
                return; \
                } \
                        var fader = document.getElementById('fader'); \
                fader.classList.remove('fade-in'); \
                }); \
        </script>"

html_footer = "</body> \
                </hmtl>"

# command line arguments
"""
page_title = str(sys.argv[1]) # name of page as string
path = sys.argv[2] # path to the page (i.e. does it involve an enclosing directory?)
all_bool = sys.arv[3] # create all three?
dir_bool = sys.arv[4] # enclose it in a folder?
"""

if __name__ == "__main__": 
    os.open("Desktop/")
 