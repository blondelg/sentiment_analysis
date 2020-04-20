# Libraries à invoquer
library(RTextTools)
library(e1071)
library(ROCR)
library(dplyr)
library(NLP)
library(tm)
library(ggplot2)
library(dplyr)
library(plyr)
library(sm)
library(FactoMineR)
library(factoextra)
library(wordcloud)

# définition du répertoire de travail
setwd("/home/jojo/Documents/Data Science/Projet")

# chargement des donnés brutes dans un objet data.frame
data_set<-read.csv("pr_10k.csv", header=TRUE, sep =";",  stringsAsFactors = FALSE)

# Division du jeu de donné par label et réarangement aléatoire des données dans chaque sous groupe
pos_data<-select(filter(data_set, sentiment == "positive"), c(1:3))[sample(nrow(select(filter(data_set, sentiment == "positive"), c(1:3)))),]
neg_data<-select(filter(data_set, sentiment == "negative"), c(1:3))[sample(nrow(select(filter(data_set, sentiment == "negative"), c(1:3)))),]

# Comptage des labels
nb_pos<-nrow(pos_data)
nb_neg<-nrow(neg_data)

# Division du jeu de donnée en ensemble d'apprentissage/ ensemble de test
pos_learn<-c(pos_data[1:round(0.7*nrow(pos_data),0),2])
pos_learn <- pos_learn[-which(pos_learn=="")]

pos_test<-c(pos_data[1+round(0.7*nrow(pos_data),0):nrow(pos_data), 2])
pos_test <- pos_test[-which(pos_test=="")]

neg_learn<-c(neg_data[1:round(0.7*nrow(neg_data),0),2])
neg_learn <- neg_learn[-which(neg_learn=="")]

neg_test<-c(neg_data[1+round(0.7*nrow(neg_data),0):nrow(neg_data), 2])
neg_test <- neg_test[-which(neg_test=="")]

# Création des vecteurs rewiews et des vecteurs labels
nb_learn = 700 # number of records to include into learn subset
nb_test = 300 # number of records to include into test subset

rev_learn=c(pos_learn[1:nb_learn], neg_learn[1:nb_learn])
sent_learn=c(rep("p", nb_learn), rep("n", nb_learn))

rev_test=c(pos_test[1:nb_test], neg_test[1:nb_test])
sent_test=c(rep("p", nb_test), rep("n", nb_test))

rev_all=c(rev_learn, rev_test)
sent_all=as.factor(c(sent_learn, sent_test))
pos_all=c(pos_learn,pos_test)
neg_all=c(neg_learn, neg_test)

# fonction de nettoyage d'un corpus
  # corpus= coprus en entrée
  # min_freq= frequence d'occurence minimale d'un mot en dessous de laquelle ce mot est exclu du corpus
cleantext <- function(corpus, min_freq){ # Fonction de nettoyage
  clean_corpus <- tm_map(corpus, removeNumbers)
  clean_corpus <- tm_map(clean_corpus, content_transformer(tolower)) 
  clean_corpus <- tm_map(clean_corpus, removePunctuation)
  clean_corpus <- tm_map(clean_corpus, removeWords, stopwords("english"))
  clean_corpus <- tm_map(clean_corpus, stripWhitespace)
  # Delete unfrequent words
  out_words<-names(subset(ffreq(clean_corpus), ffreq(clean_corpus)<min_freq))
  inf<-0
  sup<-500
  while(inf<length(out_words)){
    clean_corpus <- tm_map(clean_corpus, removeWords, out_words[inf:sup])
    inf<-inf+500
    sup<-sup+500
  }
  clean_corpus
}

# Fonction qui calcule les fréquences d'occurance des mots à partir d'une matrice
ffreq <- function(corpus){ 
  MTD <- TermDocumentMatrix(corpus)
  mat<- as.matrix(MTD)
  v <- sort(rowSums(mat),decreasing=TRUE)
  v
}

# Nettoyage des corpus
all_corpus<-cleantext(VCorpus(VectorSource(rev_all)), 0)
learn_corpus<-cleantext(VCorpus(VectorSource(rev_learn)), 0)
test_corpus<-cleantext(VCorpus(VectorSource(rev_test)), 0)

pos_corpus<-cleantext(VCorpus(VectorSource(pos_all)), 0)
neg_corpus<-cleantext(VCorpus(VectorSource(neg_all)), 0)

# Visualiser quelques éléments du corpus
learn_corpus[[10]]$content
learn_corpus[[101]]$content
learn_corpus[[210]]$content

# Corpus global: afficher les mots les plus fréquents
MTD <- TermDocumentMatrix(all_corpus)
mat<- as.matrix(MTD)
v <- sort(rowSums(mat),decreasing=TRUE)
d<- data.frame(word = names(v),freq=v)
gg <- ggplot(data=head(d, 15), aes(x=reorder(word, -freq), y=freq)) + geom_bar(stat="identity") + labs(x = "", y = "Frequence d'occurence corpus global")
plot(gg)

# Corpus par label: afficher les mots les plus fréquents
MTD <- TermDocumentMatrix(pos_corpus)
mat<- as.matrix(MTD)
v <- sort(rowSums(mat),decreasing=TRUE)
dpos <- data.frame(word = names(v),freq=v, sent=c(rep("p", length(v))))

MTD <- TermDocumentMatrix(neg_corpus)
mat<- as.matrix(MTD)
v <- sort(rowSums(mat),decreasing=TRUE)
dneg <- data.frame(word = names(v),freq=v, sent=c(rep("n", length(v))))

gg <- ggplot(data=rbind(head(dpos, 15), head(dneg, 15)), aes(x=reorder(word, -freq), y=freq, fill=sent)) + geom_bar(stat="identity") + labs(x = "", y = "Frequence d'occurence corpus par labels")
plot(gg)

# Create term doc matrix
learn_MTD<-DocumentTermMatrix(learn_corpus, control=list(weighting=weightTfIdf))
inspect(learn_MTD)

# Exemple de méthode descriptive: ACP
learn_corpus_ACP<-cleantext(VCorpus(VectorSource(c(pos_learn[1:100], neg_learn[1:100]))), 0)
ACP_MTD<-TermDocumentMatrix(learn_corpus_ACP, control=list(weighting=weightTfIdf))
temp_learn_MTD<-data.frame(as.matrix(removeSparseTerms(ACP_MTD, 0.9)))
inspect(removeSparseTerms(ACP_MTD, 0.9))
res<-PCA(temp_learn_MTD)
fviz_eig(res, addlabels = TRUE, ylim = c(0, 50))

# Naive Bayes
learn_MTD<-DocumentTermMatrix(learn_corpus, control=list(weighting=weightTfIdf))
learn_mat<-as.matrix(learn_MTD)
as.matrix(removeSparseTerms(learn_MTD, 0.99))
classifier_bayes<-naiveBayes(learn_mat, as.factor(sent_learn))

# Accuracy ensemble d'apprentissage
learn_bayes<-predict(classifier_bayes,as.matrix(removeSparseTerms(learn_MTD, 0.99)))

# Calcul de l'accuracy
recall_accuracy(sent_learn, learn_bayes)
table(learn_bayes, sent_learn)

# Prédiction:
test_MTD<-DocumentTermMatrix(test_corpus, control=list(weighting=weightTfIdf))
test_mat<-as.matrix(removeSparseTerms(test_MTD, 0.99))
predicted_bayes<-predict(classifier_bayes,test_mat)
recall_accuracy(sent_test, predicted_bayes)
predicted_bayes

# Matrice de confusion
table(predicted_bayes, sent_test)

# Calcul de l'accuracy
recall_accuracy(sent_test, predicted_bayes)

# Trouver le parametre "frequence minimum" qui optimise l'accuracy par itération de pas 15
gap<-0
min_freq_v<-c()
accuracy_v<-c()
while(gap<80){
  learn_corpus<-cleantext(VCorpus(VectorSource(rev_learn)), gap)
  test_corpus<-cleantext(VCorpus(VectorSource(rev_test)), gap)
  learn_MTD<-DocumentTermMatrix(learn_corpus, control=list(weighting=weightTfIdf))
  learn_mat<-as.matrix(learn_MTD)
  test_MTD<-DocumentTermMatrix(test_corpus, control=list(weighting=weightTfIdf))
  test_mat<-as.matrix(test_MTD)
  classifier_bayes<-naiveBayes(learn_mat, as.factor(sent_learn))
  predicted_bayes<-predict(classifier_bayes,test_mat)
  min_freq_v<-c(min_freq_v, gap)
  accuracy_v<-c(accuracy_v, recall_accuracy(sent_test, predicted_bayes))
  gap<-gap+15
  print(gap)
}

# Visualisation du résultat
opti_min<-data.frame(min_freq_v, accuracy_v)
gg<-ggplot(opti_min, aes(x=min_freq_v, y=accuracy_v)) +
  geom_point(shape=1) +    # Use hollow circles
  geom_smooth() + labs(x = "minimum frequency", y = "accuracy")
plot(gg)

# précision avec un pas plus petit
gap<-opti_min$min_freq_v[which(opti_min$accuracy_v== max(opti_min$accuracy_v))]- 10
min_freq_v<-c()
accuracy_v<-c()
while(gap<opti_min$min_freq_v[which(opti_min$accuracy_v== max(opti_min$accuracy_v))]  + 11){
  learn_corpus<-cleantext(VCorpus(VectorSource(rev_learn)), gap)
  test_corpus<-cleantext(VCorpus(VectorSource(rev_test)), gap)
  learn_MTD<-DocumentTermMatrix(learn_corpus, control=list(weighting=weightTfIdf))
  learn_mat<-as.matrix(learn_MTD)
  test_MTD<-DocumentTermMatrix(test_corpus, control=list(weighting=weightTfIdf))
  test_mat<-as.matrix(test_MTD)
  classifier_bayes<-naiveBayes(learn_mat, as.factor(sent_learn))
  predicted_bayes<-predict(classifier_bayes,test_mat)
  min_freq_v<-c(min_freq_v, gap)
  accuracy_v<-c(accuracy_v, recall_accuracy(sent_test, predicted_bayes))
  gap<-gap+2
  print(gap)
}

# Visualisation du résultat
opti_min<-data.frame(min_freq_v, accuracy_v)
gg<-ggplot(opti_min, aes(x=min_freq_v, y=accuracy_v)) +
  geom_point(shape=1) +    # Use hollow circles
  geom_smooth() + labs(x = "minimum frequency", y = "accuracy")
plot(gg)

# Naive Bayes avec optimisation du parametre freq min=19
learn_corpus_opt<-cleantext(VCorpus(VectorSource(rev_learn)), 19)
test_corpus_opt<-cleantext(VCorpus(VectorSource(rev_test)), 19)
learn_MTD<-DocumentTermMatrix(learn_corpus_opt, control=list(weighting=weightTfIdf))
learn_mat<-as.matrix(learn_MTD)
as.matrix(removeSparseTerms(learn_MTD, 0.99))
classifier_bayes<-naiveBayes(learn_mat, as.factor(sent_learn))


# Accuracy ensemble d'apprentissage
learn_bayes<-predict(classifier_bayes,as.matrix(removeSparseTerms(learn_MTD, 0.99)))

# Calcul de l'accuracy
recall_accuracy(sent_learn, learn_bayes)
table(learn_bayes, sent_learn)

# Prédiction:
test_MTD<-DocumentTermMatrix(test_corpus_opt, control=list(weighting=weightTfIdf))
test_mat<-as.matrix(removeSparseTerms(test_MTD, 0.99))
predicted_bayes<-predict(classifier_bayes,test_mat)
recall_accuracy(sent_test, predicted_bayes)
predicted_bayes

# Application a plusieurs algorythmes
all_corpus<-cleantext(VCorpus(VectorSource(rev_all)), 19)
all_MTD<-DocumentTermMatrix(all_corpus, control=list(weighting=weightTfIdf))
all_mat<-as.matrix(removeSparseTerms(all_MTD, 0.99))

# Calcul des predictions et accuracy pour l'enssemble d'apprentissage
container = create_container(all_mat, as.numeric(sent_all), trainSize = 1:(nb_learn*2), testSize = 1:(nb_learn*2), virgin = FALSE)
models = train_models(container, algorithms = c("MAXENT", "SVM", "SLDA", "RF", "TREE"))
results = classify_models(container, models)
analytics<-create_analytics(container, results)

pred_tree<-prediction(results$TREE_PROB, sent_learn)
perf_tree<-performance(pred_tree, "tpr", "fpr")
plot(perf_tree, col="blue", spread.estimate="none")

pred_svm<-prediction(results$SVM_PROB, sent_learn)
perf_svm<-performance(pred_svm, "tpr", "fpr")
plot(perf_svm, col="red", spread.estimate="none", add=TRUE)

pred_me<-prediction(results$MAXENTROPY_PROB, sent_learn)
perf_me<-performance(pred_me, "tpr", "fpr")
plot(perf_me, col="green", spread.estimate="stderror", add=TRUE)

pred_slda<-prediction(results$SLDA_PROB, sent_learn)
perf_slda<-performance(pred_slda, "tpr", "fpr")
plot(perf_slda, col="orange", spread.estimate="stderror", add=TRUE)

pred_for<-prediction(results$FORESTS_PROB, sent_learn)
perf_for<-performance(pred_for, "tpr", "fpr")
plot(perf_for, col="pink", spread.estimate="stderror", add=TRUE)

summary(analytics)

# Calcul des predictions et accuracy pour l'enssemble de test
container = create_container(all_mat, as.numeric(sent_all), trainSize = 1:(nb_learn*2), testSize = (nb_learn*2+1):(nb_learn*2 + nb_test*2), virgin = FALSE)
models = train_models(container, algorithms = c("MAXENT", "SVM", "SLDA", "RF", "TREE"))
results = classify_models(container, models)
analytics<-create_analytics(container, results)

pred_tree<-prediction(results$TREE_PROB, sent_test)
perf_tree<-performance(pred_tree, "tpr", "fpr")
plot(perf_tree, col="blue", spread.estimate="stderror", add=TRUE)

pred_svm<-prediction(results$SVM_PROB, sent_test)
perf_svm<-performance(pred_svm, "tpr", "fpr")
plot(perf_svm, col="red", spread.estimate="stderror", add=TRUE)

pred_me<-prediction(results$MAXENTROPY_PROB, sent_test)
perf_me<-performance(pred_me, "tpr", "fpr")
plot(perf_me, col="green", spread.estimate="stderror", add=TRUE)

pred_slda<-prediction(results$SLDA_PROB, sent_test)
perf_slda<-performance(pred_slda, "tpr", "fpr")
plot(perf_slda, col="orange", spread.estimate="stderror", add=TRUE)

pred_for<-prediction(results$FORESTS_PROB, sent_test)
perf_for<-performance(pred_for, "tpr", "fpr")
plot(perf_for, col="pink", spread.estimate="stderror", add=TRUE)


summary(analytics)

# Modele maison
min_freq<-19

# Calcul de la fréquence d'occurance des mots dans le corpus positif
pos_corpus<-cleantext(VCorpus(VectorSource(rev_learn[1:nb_learn])), 0)
mot_pos<-subset(ffreq(pos_corpus), ffreq(pos_corpus)>min_freq)
mot_pos<-mot_pos/length(pos_corpus)

# Calcul de la fréquence d'occurance des mots dans le corpus negatif
neg_corpus<-cleantext(VCorpus(VectorSource(rev_learn[(nb_learn+1):(nb_learn*2)])), 0)
mot_neg<-subset(ffreq(neg_corpus), ffreq(neg_corpus)>min_freq)
mot_neg<-mot_neg/length(neg_corpus)

# Création du data frame 
freq_pos<-data.frame(names(mot_pos),mot_pos,rep(0, length(mot_pos)))
colnames(freq_pos)<-c("mot","freq_pos", "freq_neg")
freq_neg<-data.frame(names(mot_neg),rep(0,length(mot_neg)),mot_neg)
colnames(freq_neg)<-c("mot","freq_pos", "freq_neg")

freq<-data.frame(rbind(freq_pos, freq_neg))
freq<-ddply(freq,~mot,summarise,freq_pos=sum(freq_pos),freq_neg=sum(freq_neg))
freq<-data.frame(freq, rep("no", nrow(freq)))
colnames(freq)<-c("mot", "pos", "neg", "is_cr")

# Ploter le nuage de point frequence
p <- ggplot(data=freq, aes(x=pos, y=neg))
p <- p + geom_point(size=1, alpha = 1/3) + geom_abline(intercept = 0, slope = 1)
print(p)

# Centrer réduire les données
freq_cr<-data.frame(freq$mot, scale(freq$pos, center = TRUE, scale = TRUE), scale(freq$neg, center = TRUE, scale = TRUE), rep("yes", nrow(freq)))

# Calculer la discance a la bissectrice
colnames(freq_cr)<-c("mot", "pos", "neg", "is_cr")


p <- ggplot(data=freq_cr, aes(x=pos, y=neg))
p <- p + geom_point(size=1, alpha = 1/3) + geom_abline(intercept = 0, slope = 1)
print(p)

freq<-rbind(freq, freq_cr)
p <- ggplot(data=freq, aes(x=pos, y=neg, colour=is_cr))
p <- p + geom_point(size=0.5, alpha = 1/3) + geom_abline(intercept = 0, slope = 1)
print(p)

# calculer les distances et positions
dist_x<-c(freq_cr$pos)
dist_y<-c(freq_cr$neg)

# Calcul de la norme du score_D
dist_cr<-c(sqrt(2*(dist_x-dist_y)^2)/2)
freq_cr<-data.frame(freq_cr, dist_cr)

position<-c(ifelse(freq_cr$pos>freq_cr$neg, "pos", "neg"))
freq_cr<-data.frame(freq_cr, position)

# Calcul du score_D
pos_rel<-c(ifelse(freq_cr$position == "pos", freq_cr$dist_cr, -freq_cr$dist_cr))
freq_cr<-data.frame(freq_cr, pos_rel)

p <- ggplot(data=freq_cr, aes(x=pos, y=neg, colour=position))
p <- p + geom_point(size=0.8, alpha = 1/2) + geom_abline(intercept = 0, slope = 1)
p <- p + labs(x = "fréquence corpus positif", y = "fréquence corpus négatif")
print(p)

# Nuage des mots par distance (les plus differenciants)
# La taille des mots est proportionnelle à la norme du Score_D, la couleur correspond au corpus représenté
Colors<-c(ifelse(freq_cr$position=="pos", "green", "red"))
set.seed(300)
wordcloud(words = freq_cr$mot, freq = freq_cr$dist_cr, scale = c(3, 0.3) ,min.freq = 0,
          max.words = 300, random.order = FALSE, rot.per = 0.2, vfont=c("sans serif","plain"),
          colors=Colors, ordered.colors=TRUE)

# Graphique des densités des normes des Score_D
p <- ggplot(freq_cr, aes(dist_cr, fill = position, colour = position)) 
p <- p + geom_density(alpha = 0.1)
p <- p + labs(x = "|Score_D|", y = "Densité")
print(p)

# Ajouter un indice
pos_rel<-c(ifelse(freq_cr$position == "pos", freq_cr$dist_cr, -freq_cr$dist_cr))
freq_cr<-data.frame(freq_cr, pos_rel)
pos_rel_cr <-c(scale(freq_cr$pos_rel, center = TRUE, scale = TRUE))
freq_cr<-data.frame(freq_cr, pos_rel_cr)

# Densité de la distribution du Score_D
p <- ggplot(freq_cr, aes(pos_rel_cr)) + geom_density(alpha = 0.1)
p <- p + stat_function(fun = dnorm, args = list(mean = 0, sd = 0.5))
p <- p + labs(x = "Score_D", y = "Densité")
print(p)

# Fonction score, calcule le score d'un commentaire
score <- function(comment){
  ctest<-c(comment)
  corpus_test<-VCorpus(VectorSource(ctest))
  corpus_test<-cleantext(corpus_test, 0)
  MTD_test<-TermDocumentMatrix(corpus_test)
  mat <- as.matrix(MTD_test)
  coef<-c(freq_cr[freq_cr$mot %in% rownames(mat), ]$pos_rel_cr)
  nb <- c(mat[rownames(mat) %in% freq_cr$mot, 1])
  result<-sum(coef*nb)
  result
}

# Calcul des scores en apprentissage
score_vect<-c()
for(i in seq(1, length(sent_learn))){
  score_vect <- c(score_vect, score(rev_learn[i]))
}

# Calcul des probas en apprentissage
learn_df$proba <- NULL
proba_p <-c()
for(i in seq(1, length(sent_learn))){
  proba_p <- c(proba_p, pnorm(score_vect[i] , mean=0, sd=0.5))
}
learn_df <- data.frame(rev_learn, sent_learn, score_vect,proba_p, ifelse(proba_p > 0.5, "p", "n"))
colnames(learn_df) <- c("rev_learn","sent_learn","score_vect","proba","predict_sent")

# Matrice de confusion
table(learn_df$sent_learn,learn_df$predict_sent )
recall_accuracy(learn_df$sent_learn,learn_df$predict_sent)


# Calcul des scores en test
score_vect<-c()
for(i in seq(1, length(sent_test))){
  score_vect <- c(score_vect, score(rev_test[i]))
}

# Calcul des probas en test
test_df$proba <- NULL
proba_p <-c()
for(i in seq(1, length(sent_test))){
  proba_p <- c(proba_p, pnorm(score_vect[i] , mean=0, sd=0.5))
}
test_df <- data.frame(rev_test, sent_test, score_vect,proba_p, ifelse(proba_p > 0.5, "p", "n"))
colnames(test_df) <- c("rev_test","sent_test","score_vect","proba","predict_sent")



# Matrice de confusion
table(test_df$sent_test,test_df$predict_sent )
recall_accuracy(test_df$sent_test,test_df$predict_sent)

pred_for<-prediction(learn_df$proba, sent_learn)
perf_for<-performance(pred_for, "tpr", "fpr")
plot(perf_for, col="purple", spread.estimate="stderror", add=TRUE)

pred_for<-prediction(test_df$proba, sent_test)
perf_for<-performance(pred_for, "tpr", "fpr")
plot(perf_for, col="purple", spread.estimate="stderror", add=TRUE)

# Courbe ROC finale:

# Calcul des predictions et accuracy pour l'enssemble d'apprentissage
container = create_container(all_mat, as.numeric(sent_all), trainSize = 1:(nb_learn*2), testSize = 1:(nb_learn*2), virgin = FALSE)
models = train_models(container, algorithms = c("MAXENT", "SVM", "SLDA", "RF", "TREE"))
results = classify_models(container, models)
analytics<-create_analytics(container, results)

pred_tree<-prediction(results$TREE_PROB, sent_learn)
perf_tree<-performance(pred_tree, "tpr", "fpr")
plot(perf_tree, col="blue", spread.estimate="none")

pred_svm<-prediction(results$SVM_PROB, sent_learn)
perf_svm<-performance(pred_svm, "tpr", "fpr")
plot(perf_svm, col="red", spread.estimate="none", add=TRUE)

pred_me<-prediction(results$MAXENTROPY_PROB, sent_learn)
perf_me<-performance(pred_me, "tpr", "fpr")
plot(perf_me, col="green", spread.estimate="stderror", add=TRUE)

pred_slda<-prediction(results$SLDA_PROB, sent_learn)
perf_slda<-performance(pred_slda, "tpr", "fpr")
plot(perf_slda, col="orange", spread.estimate="stderror", add=TRUE)

pred_for<-prediction(results$FORESTS_PROB, sent_learn)
perf_for<-performance(pred_for, "tpr", "fpr")
plot(perf_for, col="pink", spread.estimate="stderror", add=TRUE)

container = create_container(all_mat, as.numeric(sent_all), trainSize = 1:(nb_learn*2), testSize = (nb_learn*2+1):(nb_learn*2 + nb_test*2), virgin = FALSE)
models = train_models(container, algorithms = c("MAXENT", "SVM", "SLDA", "RF", "TREE"))
results = classify_models(container, models)
analytics<-create_analytics(container, results)

pred_tree<-prediction(results$TREE_PROB, sent_test)
perf_tree<-performance(pred_tree, "tpr", "fpr")
plot(perf_tree, col="blue", spread.estimate="stderror", add=TRUE)

pred_svm<-prediction(results$SVM_PROB, sent_test)
perf_svm<-performance(pred_svm, "tpr", "fpr")
plot(perf_svm, col="red", spread.estimate="stderror", add=TRUE)

pred_me<-prediction(results$MAXENTROPY_PROB, sent_test)
perf_me<-performance(pred_me, "tpr", "fpr")
plot(perf_me, col="green", spread.estimate="stderror", add=TRUE)

pred_slda<-prediction(results$SLDA_PROB, sent_test)
perf_slda<-performance(pred_slda, "tpr", "fpr")
plot(perf_slda, col="orange", spread.estimate="stderror", add=TRUE)

pred_for<-prediction(results$FORESTS_PROB, sent_test)
perf_for<-performance(pred_for, "tpr", "fpr")
plot(perf_for, col="pink", spread.estimate="stderror", add=TRUE)

pred_for<-prediction(learn_df$proba, sent_learn)
perf_for<-performance(pred_for, "tpr", "fpr")
plot(perf_for, col="purple", spread.estimate="stderror", add=TRUE)

pred_for<-prediction(test_df$proba, sent_test)
perf_for<-performance(pred_for, "tpr", "fpr")
plot(perf_for, col="purple", spread.estimate="stderror", add=TRUE)
