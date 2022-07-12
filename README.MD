build le conteneur avec cette commande 
❯ docker build . -t exec1                                                                                                                                                                                                            ─╯
lancer le contenaire comme suit 
❯ docker run --privileged  -it -p 8000:8000  -v /var/run/docker.sock:/var/run/docker.sock exec1                                                                                                                                 ─╯
