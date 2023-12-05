1. Implement an application that exposes this [JSON] document when visited with an HTTP client:
   ```json
   { "id": "1", "message": "Hello world" }
   ```
2. Containerize with [Docker]the application.
3. Create a second application that reverses the `message` of the HTTP response from the first service as JSON. Note that JSON must be dynamically rendered and is not a static string.
      ```json
      { "id": "1", "message": "dlrow olleH" }
      ```
4. Containerize the second application.
5. Run both applications in [Minikube](https://minikube.sigs.k8s.io/docs/), [Kind](https://kind.sigs.k8s.io/), or any other suitable solution to run [Kubernetes](https://kubernetes.io/) locally.  
  You can use your preferred tool to define the [YAML](https://yaml.org/) manifests for Kubernetes, for example [Helm](https://helm.sh/), [Kustomize](https://kustomize.io/), [Jsonnet](https://jsonnet.org/), [YTT](https://carvel.dev/ytt/), [Cue](https://cuelang.org/) or [Cdk8s](https://cdk8s.io/).  
  Note: The communication between the two applications must occur internally in the cluster. The proposed solution should be able to work on a real cluster as well (up to reasonable adaptations)
6. Automate deployment of the two applications in the cluster using a script (called `script.sh`).  
   - build and push the Docker image.
   - deploy applications to Kubernetes.
   - print HTTP responses of applications.# message-reversal-app
