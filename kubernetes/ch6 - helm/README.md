# Tutorial 
[youtube](https://youtu.be/-ykwb1d0DXU)

# helm chart 
- 3 deployments
- 3 services
- 1 ingress
- secret 
- configMap

```

helm create djangohelm

# Sans valeurs
helm install django-test djangohelm/ --namespace u-9nl7s

# Avec valeurs
helm upgrade django-test djangohelm/ --namespace u-9nl7s --values ./djangohelm/values.yaml

# test 

helm template django-test djangohelm/ --namespace u-9nl7s --values ./djangohelm/values.yaml >> test.yaml

# Vider mon namespace
monkube delete all --all -n u-9nl7s
```
# loop dans help 
- Attention a ne pas oublier (---) pour bien separer les ressources
```
{{- range .Values.services }}
---
```
- a mettre aussi les valeurs entre ("") 
```
value: "{{ .value }}"
```

# output 
```
Location: /home/slim/.kube/config
NAME: django-test
LAST DEPLOYED: Wed Nov 20 11:06:05 2024
NAMESPACE: u-9nl7s
STATUS: deployed
REVISION: 1
TEST SUITE: None

```