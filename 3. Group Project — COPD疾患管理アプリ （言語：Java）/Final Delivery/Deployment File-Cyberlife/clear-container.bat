docker stop cim-app
docker stop cim-web
docker stop cim-nginx
docker stop cim-mysql
docker rm cim-app
docker rm cim-web
docker rm cim-nginx
docker rm cim-mysql
docker rmi copdidentifymanage_app
docker rmi copdidentifymanage_web
docker rmi copdidentifymanage_nginx