FROM nginx:alpine

# remove exists ngix conf and add my own nginx conf
RUN rm /etc/nginx/conf.d/default.conf
ADD default.conf /etc/nginx/conf.d/default.conf