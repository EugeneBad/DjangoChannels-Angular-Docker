resource "google_compute_route" "private-to-nat-route" {
  name        = "private-to-nat-route"
  dest_range  = "0.0.0.0/0"
  network     = "${google_compute_network.djchangular-vpc.name}"
  next_hop_instance = "${google_compute_instance.k8smaster-nat-instance.name}"
  priority    = 100
  tags = ["db"]
  next_hop_instance_zone = "asia-south1-a"
}