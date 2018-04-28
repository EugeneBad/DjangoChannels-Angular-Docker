resource "google_compute_instance_group_manager" "k8sclstr-ig-manager" {
  name = "k8sclstr-ig-manager"
  zone = "asia-south1-a"
  description = "k8sclstr minion instance group"
  instance_template  = "${google_compute_instance_template.k8sclstr-template.self_link}"
  base_instance_name = "k8sclstr-minion"

  named_port {
    name = "backend-port"
    port = 30003
  }

  named_port {
    name = "frontend-port"
    port = 30002
  }
}