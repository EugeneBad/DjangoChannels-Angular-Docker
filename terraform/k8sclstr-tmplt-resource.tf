resource "google_compute_instance_template" "k8sclstr-template" {
  name = "k8sclstr-template"
  description = "Template for the k8s cluster minions"
  machine_type = "n1-standard-1"
  tags = ["private"]

  disk {
    source_image = "k8scluster-base-image"
  }

  network_interface {
    subnetwork = "${google_compute_subnetwork.private-subnetwork.name}"
  }

  metadata_startup_script = "kubeadm join 10.0.0.2:6443 --token 81ylqd.rcjxmfjgnf6rfuxx --discovery-token-ca-cert-hash sha256:e539b3738e93bc09f5a86b90568c71580adc8148e97efead8cc732f416c46bca"

}