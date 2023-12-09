apiVersion: apps/v1
kind: Deployment #object type
metadata:
    name: myapp-deployment #Deployment name
    labels: #Deployment labels
        app: myapp
        type: front-end
spec:
    replicas: 3 #Number of replicas
    selector: #POD taged with these labels will be handled by the Deployment
        matchLabels:
            app: myapp
            type: front-end
    template: #POD definition file
        metadata:
            name: myapp-pod #Pod name
            labels:
                app: myapp
                type: front-end
        spec:
            containers:
            - name: nginx-conatiner
              image: ngnix