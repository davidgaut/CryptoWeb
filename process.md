
# # Settings and packages
# virtualenv CloudComputing
# source CloudComputing/bin/activate

# pip install pipreqs
make requirements.txt
pipreqs
# Install required
pip install -r requirements.txt

# Take to browser
http://localhost:8000/ 

curl http://localhost:8001/version

# kubectl
kubectl version
kubectl get nodes/services/rs
kubectl create deployment
kubectl get deployments

kubectl describe pods
# create procy to interact with pods (isolated in a private network)
kubectl proxy
kubectl logs $POD_NAME
kubectl exec $POD_NAME -- env