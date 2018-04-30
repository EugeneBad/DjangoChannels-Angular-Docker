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

  metadata_startup_script = "sudo ${var.k8scluster-join-hash}"

}