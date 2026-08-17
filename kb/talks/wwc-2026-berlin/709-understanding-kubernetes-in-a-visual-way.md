---
id: 709
title: "Understanding Kubernetes in a visual way"
slug: understanding-kubernetes-in-a-visual-way
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Cloud & AI Infrastructure"
type: "Keynote/Talk"
stage: "Stage 5"
tags: ["Containers"]
speakers: ["Aurélie Vache"]
speaker_companies: ["OVHcloud"]
day: 1
starts_at: 2026-07-09T12:10:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=8uTU388vyVU
video_id: 8uTU388vyVU
session_page: https://app.wearedevelopers.com/events/16/session/709
transcript: true
---

# Understanding Kubernetes in a visual way

**Aurélie Vache (Developer Advocate — OVHcloud)**

`Track: Cloud & AI Infrastructure` · `Type: Keynote/Talk` · `Stage: Stage 5`

`#Containers`

[Watch the recording](https://www.youtube.com/watch?v=8uTU388vyVU) · [Session page](https://app.wearedevelopers.com/events/16/session/709)

## Abstract

Kubernetes has become the de-facto standard to deploy and operate containerized applications. But understanding Kubernetes can be difficult or time-consuming.

Several years ago I asked myself how I imagined the concepts of Kubernetes: a pod, a deployment, a service, a secret, a configmap, a cronjob… and then I created a new way of explaining Cloud technologies.

In the first part of the talk, I will tell you a story, I will tell you my story. How, during more than two years, I worked every evening/nights/week-end to explain Kubernetes in sketchnotes, in blog posts, videos and finally published everything (and more) in an illustrated book of more than 270 pages (with all the concepts included Debugging / Troubleshooting and Tips) and why I continue to do it.

And in the second part, I will explain Kubernetes concepts to you ... in a visual way :-).

## Speakers

### Aurélie Vache

*Developer Advocate — OVHcloud*

Aurélie Vache is a Developer Advocate at OVHcloud in Toulouse, France. She is Docker Captain, CNCF ambassador, Google Cloud Developer Expert, Women techmarkers Ambassador & GitPod Hero. She has been working as a Developer and Ops for over 18 years. Cloud enthusiast and advocates DevOps/Cloud/Golang best practices.

Conferences and meetups organizer since 2016. Technical writer (dev.to/aurelievache), a book author & reviewer, a sketchnoter and a speaker at international conferences.

Mentor and promote diversity and accessibility in technology.

She created a new visual way for people to learn and understand Cloud technologies: "Understanding Kubernetes/Istio/Docker in a visual way" in sketchnotes, books and videos.

Blog: https://dev.to/aurelievache/
YouTube: https://www.youtube.com/c/AurelieVache

## Transcript

*3,099 words · source: yt (en)*

**[0:03](https://www.youtube.com/watch?v=8uTU388vyVU&t=3s)** Hi buddy and welcome at I think Kubernetes visual way. I'm already much I'm developer advocate at Rancher Cloud to specialize in Kubernetes communities, containers as a first rate code and deployments. And what I like is trying to make complex technologies accessible to everyone. So Kubernetes has become the de facto standard in the containers acquisition world. We heard about it everyday. But it can be difficult and time consuming to understand Kubernetes. And it is not easy to know where and how to start. So maybe a new way of running can help us to understand Kubernetes. What if I tell you that several years

**[0:50](https://www.youtube.com/watch?v=8uTU388vyVU&t=50s)** ago I have written a new way of explaining Kubernetes visually? That's it. I will tell you a story. I tell you my little story. In 2020 during the first lockdown I laid down on my bed one Saturday or Sunday um afternoon. I took my old tablet and I imagine from and I wonder of um how I imagine a pod, one of the concept of Kubernetes and I started swimming a Pokéball. For me a pod is like a Pokéball and inside you can have one or several containers and I started swimming what

**[1:39](https://www.youtube.com/watch?v=8uTU388vyVU&t=99s)** to see in my screen. Well, it wasn't very very beautiful but it was the beginning of a great um adventure. Then I took it it might be time for me to realize an idea I have to give some tips information on Kubernetes and writing in drawing, useful, not useful, already seen, should I give up? Well, you can see in the last sentence the confidence I have in what I do, but I have but I got a lot of reaction tell me that it was cool, and then I continue. Kubernetes for me is a long time story. When I was when I was working for an auto automobile company,

**[2:28](https://www.youtube.com/watch?v=8uTU388vyVU&t=148s)** I discovered Kubernetes there is a seven years seven eight years ago. I develop and deploy microservice for Kubernetes and autonomous vehicle, and I fell into Kubernetes very quickly. So, I sketch note Kubernetes every day every morning for months and months and months, and in fact I realized that I had the impression that I felt that there were lot of thing in my head that I had to get them out by sketching. Three months later, I created the first version of an ebook about Kubernetes with some drawing.

**[3:16](https://www.youtube.com/watch?v=8uTU388vyVU&t=196s)** After some times, I wanted to do better, so I changed my tablet, and I wrote uh everything, and I added a 150 new pages, and then I created my own book in a paper paper paperback. I went even further by making a short video on YouTube, and I put a link in a two three minute video with a mix of sketch notes and and and video. And I still continued to create a new sketch notes every week or months depending on the new releases about

**[4:05](https://www.youtube.com/watch?v=8uTU388vyVU&t=245s)** Kubernetes. Okay, it's good, but why explaining in the when but why explaining in the different way is important? Because there are currently 8 billion people 8 billion people on Earth. We are all different. We all think differently. We don't have the same logic. We don't have the same way of thinking. And there are uh around 15% of people neuroatypical diagnosed in the world and there are more. And the majority of books are done the same way. They all look the same. It's a one big It's not uh AI 2021.

**[4:53](https://www.youtube.com/watch?v=8uTU388vyVU&t=293s)** So, yes. A lot of books are done in the same way. So, we need different way to learn new things, okay? So, now we'll try to answer questions in a visual way. Let's start with the beginning. What is Kubernetes? Kubernetes is an open source container orchestrator. Well, no. That That doesn't explain that. Imagine Kubernetes as an orchestra conductor. Declaratively, we ask the orchestra what we want and Kubernetes will do everything possible to ensure that this request is always respected. It will manage the resources, the machines, and

**[5:42](https://www.youtube.com/watch?v=8uTU388vyVU&t=342s)** the communication between containers both externally and internally. To do this, we will write YAML manifest. These are partitions that Kubernetes must follow. Kubernetes is based on several components. The The control plane contains several internal components such as the ETCD, the scheduler, the controller manager, and the API server that expose the API of the Kubernetes clusters. Please note that when you use a managed Kubernetes cluster with a cloud provider, the control plane will be managed by the

**[6:29](https://www.youtube.com/watch?v=8uTU388vyVU&t=389s)** cloud provider. You You don't have to uh You don't have to manage it to update it. You just have to focus on the developing and the deploying of your apps in the cluster. And in the data plane, you have kubelet and kube-proxy, which run on each node. We can We can interact with the API server of the Kubernetes cluster with kubectl, a command line tool. A CLI. A little disclaimer. I said kubectl, but we can pro-

**[7:19](https://www.youtube.com/watch?v=8uTU388vyVU&t=439s)** pronounce it kubectl, kube, kube control. It doesn't matter. The most important thing is is to use it. Okay. So, we will try to explain several concepts in a visual way step by step. Let's start by the node. A node is a physical or virtual machine. A node provides CPU or GPU, memory, storage, and network connectivity. Each node contains the services needed to run pods, such as the container runtime or

**[8:08](https://www.youtube.com/watch?v=8uTU388vyVU&t=488s)** kubelet. Okay? Now, let's speak about pods. Our applications, our workload, will run in containers, which themselves run in pods. Kubernetes is language agnostic, which means that you can develop your microservice in a lot of language, like in Java, Python, Go, etc. A pod is the smallest deployable unit in a Kubernetes cluster. A pod can contain one or several co-containers, and each pod has a unique IP

**[8:58](https://www.youtube.com/watch?v=8uTU388vyVU&t=538s)** address. Our applications run in pods, which themselves run in nodes. Okay, so it's cool, but what is happening when you ask Kubernetes to create a new pod? Hey Kubernetes, create a create a create a pod, please. First, the API server receives the request and do some checks. It verifies the identity of the user. It's the authentication step. Who are you? And it check also if the user have the sufficient right to do it. If the authorization

**[9:46](https://www.youtube.com/watch?v=8uTU388vyVU&t=586s)** step. Are you guys all right? Then it save the state in the ETCD distributed then database. At the time the API server will call the scheduler. That will search which node, which machine is more convenient to place it according to CPU, GPU, memory, networks, and so on. Scheduler can do it, but in order to help him, it's useful to define request in containers of a pod. Thanks to that the pod will be placed in the correct node.

**[10:33](https://www.youtube.com/watch?v=8uTU388vyVU&t=633s)** Once placed by the scheduler, the pod is in pending state. Then kubelet will attempt to pull the image from registry. Once the image is retrieved kubelet creates the containers and starts them. Then the pod is in running status and your application is finally started and and running. Okay? I cannot speak about Kubernetes without giving some tips. So, if you want to display the specific information of about a pod, you can type kubectl get pod and with JSON path you can

**[11:22](https://www.youtube.com/watch?v=8uTU388vyVU&t=682s)** display all the image of all the containers of a pod. And you can delete immediately immediately your pods with force and grace period command. >> Okay. >> So, next let's talk about deployments. Deployments are responsible for the pod they manage. Stop. So, if a pod become um unhealthy it will create a new pod and delete the old one. Bye-bye. A deployment creates a replication a replication set which will create one or several pods depending on the of the

**[12:14](https://www.youtube.com/watch?v=8uTU388vyVU&t=734s)** number of specified replicas. By scaling a deployment, we can easily change its its number of replicas. So, with the command kubectl scale we can scale the number of replicas to five. So, the deployment will create one pod and one new pod. So, at the end of the execution of the command, the new number of replicas will be equal to five. So, Kubernetes will ensure that at every moment we will have five pods for this deployment. And of course, you can scale down at every moment.

**[13:01](https://www.youtube.com/watch?v=8uTU388vyVU&t=781s)** Okay? So, now let's talk about services. Our application running pods and this pod are ephemeral. Services allow allow us to access our application via unique IP address. So, we will be able to assign a unique DNS name to a group of pod. This will allow us to access our my zone application. So, if I do a curl in my zone application dot my name space dot as you see that the console that the local the traffic will be route to the service and and the

**[13:49](https://www.youtube.com/watch?v=8uTU388vyVU&t=829s)** from traffic will go to one pod. The group of pod targeted by a service is usually determined by a sector. This is Several type of services exist. Cluster IP is the default service type. It allows you to expose a service through an IP address internal to the cluster. So, please note that that this type of service will only be accessible within the cluster. The node port will be accessible outside the cluster but with the IP of the node. The load balancer service I find a fixed

**[14:40](https://www.youtube.com/watch?v=8uTU388vyVU&t=880s)** IP address and create an external load balancer. So, this solution only works with external cloud provider. So, in this example, we have our application running in a pod that is exposed through a service. An external load balancer have been created and IP address have been created too. So, if I do a curl there I will have my application. And the external name of service allows allows you to provide an internal alias for the clusters that would like to an external DNS

**[15:28](https://www.youtube.com/watch?v=8uTU388vyVU&t=928s)** address. Okay. Now, we we will talk about namespace. What is it? A namespace is a form of isolation. This allow you to isolate your application by project, by team, or by family of component. Resource name but must be unique within a single namespace, but not across several namespace. So, you can't have two resources with the same name in a name- namespace. That's possible. So, So, so So, you can have a one one service called my my service my service in namespace one and in namespace two, but you can't have the

**[16:17](https://www.youtube.com/watch?v=8uTU388vyVU&t=977s)** same name in the same name- name- namespace. And be careful if you delete a namespace, all resources all resources inside will be deleted as well. It's a normal behavior, but it's useful to know it. If you delete it, all the objects inside will be will be deleted as well. And not all resources in in Kubernetes are in a name- namespace. There are some objects like a node that is cluster-wide. Okay. After the namespace, let's explain what is a quota, a resource quota. The resource quota limits the use and

**[17:09](https://www.youtube.com/watch?v=8uTU388vyVU&t=1029s)** the number of resources that can be created and managed in a name- namespace. When several work on several the namespaces, a quota can be created for each the namespace. With this example, it means that on the my namespace one, we won't be able to deploy more than four pods. And on my namespace two, we define the total CPU and memory consumed by all the pod in the namespace. And we can also control the maximum number of secrets or volumes and so on. When requesting the creation of a new object, the admission controller check whether the quota will be

**[17:58](https://www.youtube.com/watch?v=8uTU388vyVU&t=1078s)** exceeded. If so, an error message is displayed and the creation will be refused. Warning, if a quota is enabled with CPU and memory, you must specify request and limits for your pods. Now, let's talk about jobs. A job is a process that takes a certain amount of time to execute. For example, a job can be created for several use cases, a batch process, a backup, a database migration, or a cleanup. A job run one on one or several pods and ensure that a specific number of pods complete successfully. So,

**[18:48](https://www.youtube.com/watch?v=8uTU388vyVU&t=1128s)** currently, a pod created by a job have a mission and it's needed to complete it. A job can be executed once, it can be sequential, or it can launch several pods in parallel. If the pod fails, another pod will run until the number of pod successfully complete. By default, completion is is set it to one. So, if we set completion to three, the job controller will spawn pods until the number of completion is reached. And jobs can be

**[19:38](https://www.youtube.com/watch?v=8uTU388vyVU&t=1178s)** indexed. It means that you can configure a job that will run several pods that will process a different chunk of data. And as pod as launched by job, for example, if the if the pod responsible to process a certain chunk of data is what? Failed. Another pod will be created until its mission is complete. Now, let's talk about cron jobs. Cron jobs allows you to launch scheduled task. Basically, so a cron job launch a job

**[20:28](https://www.youtube.com/watch?v=8uTU388vyVU&t=1228s)** which can launch one or several pods. It's useful, for example, for database backup, clean up task, and any type of periodic task like a mail sender. It is based on a cron format. Okay. So, our application run in pods controlled by a deployment that are exposed through services. And I can launch launch some batch processes, but what about the configuration and what about the environment variables? Let's talk about config map.

**[21:17](https://www.youtube.com/watch?v=8uTU388vyVU&t=1277s)** Config map answered to one of the 12 factor app for parents of microservice. Do not hardcode configuration in your apps. Instead, the best practice is to store non-sensitive data in a config map. This allows This allows you to separate configuration from pods. And thanks to that, you can deploy a same application in different environment. So, you can deploy an app in production, staging, QA, and so on. So, for example, you can define a particular configuration parameter for staging

**[22:06](https://www.youtube.com/watch?v=8uTU388vyVU&t=1326s)** environment and other one for the production. So, for example, the URL and the port of option to the base will be different. A config map can contains a config configuration files like a config.properties or or an engine accounts or one or several key-value pairs, one or several environment variables, or a binary that is encoded in base64. We can create a config map from three different sources. From a key-value. So, for for for example, we have a config map named my

**[22:56](https://www.youtube.com/watch?v=8uTU388vyVU&t=1376s)** CM and we can define some parameters like the like a threshold and maximum quantity of connection for for a DB. We can also create a config map from a file. So, there So, there like there is an example with an engine x config file. And we can also create one for an environment variable. So, we can list one or several environment variables. For example, with the host of the DB and at the port. To prevent accidental

**[23:45](https://www.youtube.com/watch?v=8uTU388vyVU&t=1425s)** or unwanted change, a config map can be can be an immutable. It can be convenient because an application should only need to read a configuration. But, it means that if you want to update the config map, you have to um you have to restart the the pod. So, it's So, it's very use- useful, but not really used now. Be careful. A pod that is in the namespace A cannot read a config map that is in an

**[24:34](https://www.youtube.com/watch?v=8uTU388vyVU&t=1474s)** another name- namespace. It is ne- necessary that the resources related to a pod are in the same name- namespace. It's really important. And the last concept we'll see today is the secret. Secrets allow you to save sensitive data such as password, token, credential, access key, or certificate. The secrets are encoded in base in base 64 and automatically decoded when read and attached to a pod. Warning, unencoded is not something like encrypted. So, the secrets are not really secrets in a Kubernetes

**[25:24](https://www.youtube.com/watch?v=8uTU388vyVU&t=1524s)** cluster. So, if someone retrieves a secret, he or she just have to decode it in in base 64. Well, it's not really really really easy because you have to get a secret with the name of the namespace, with name of the secret. You have to output it in JSON, and you have to know what is the sub field in secret, and then you have to decode it. It's not really easy. But, I have a a tips. You can use the kubectl view secret plugin. It it it can

**[26:12](https://www.youtube.com/watch?v=8uTU388vyVU&t=1572s)** help you to to type this kind of command, and it's really really really really good. Like a config map, you can create a secret for three different sources, from one or several key and value, from a file, or from an environment variable file. There are three types of secrets, generic, Docker registry, and TLS. Generic is a secret created from a file. There. Docker registry is a Docker config secret that allows a pod to authenticate to a Docker registry. And TLS is for TLS or mutual TLS certificate.

**[27:00](https://www.youtube.com/watch?v=8uTU388vyVU&t=1620s)** Like a config map, a pod that is in that is in the namespace A country the secret that is in um the Facebook. Okay? A lot of concepts exist, but my time is uh is uh almost uh over now. And the good thing is that everything we saw, we can do it for example at oh at OVH Cloud. We have a solution of managed Kubernetes clusters, and we have also a solution to uh to store your to store your Docker in in images. And also, you can manage all of your Kubernetes

**[27:51](https://www.youtube.com/watch?v=8uTU388vyVU&t=1671s)** clusters even if they are Google, Amazon, or Microsoft. And you can deploy your Kubernetes cluster with Terraform, with Pulumi, and with a CLI. Okay. To con- conclude, by listening to my creativity and my imagination during a not easy period of my life, I created a new way of explaining complicated technical concepts, and I showed that it it was possible. And I realized that my way of explaining could help other people of different job and ages and con- and continents.

**[28:39](https://www.youtube.com/watch?v=8uTU388vyVU&t=1719s)** And my purpose of this talk is to encourage you to listen to your own imagination and your own creativity and share it them other ways. So, it's really important to find your personal way to share. Thank you. Thank you. >> [applause]
