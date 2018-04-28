resource "google_compute_instance" "db-instance" {
  name         = "db-instance"
  machine_type = "n1-standard-1"
  zone         = "asia-south1-a"
  tags = ["private"]
  description = "Linux instance that hosts the database"
  depends_on = ["google_compute_instance.k8smaster-nat-instance"]
  boot_disk {
    initialize_params {
      image = "db-base-image"
    }
  }

  network_interface {
    subnetwork = "${google_compute_subnetwork.private-subnetwork.name}"
    address = "${google_compute_address.db-address.address}"
  }
}