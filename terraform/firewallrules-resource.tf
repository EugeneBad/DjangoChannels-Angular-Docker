resource "google_compute_firewall" "allow-public-firewallrule" {
  name    = "allow-public-firewallrule"
  network = "${google_compute_network.djchangular-vpc.name}"
  description = "Firewall rule that opens http port(80) on the public instance"

  allow {
    protocol = "icmp"
  }

  allow {
    protocol = "tcp"
    ports    = ["22"]
  }

  source_ranges = ["0.0.0.0/0"]
  target_tags = ["public"]
}

resource "google_compute_firewall" "allow-minion-firewallrule" {
  name = "allow-minion-firewallrule"
  network = "${google_compute_network.djchangular-vpc.name}"
  description = "Firewall rule to allow traffic from the target-proxy and healthcheck to the minion instance group"

  allow {
    protocol = "icmp"
  }

  allow {
    protocol = "tcp"
  }

  source_ranges = ["130.211.0.0/22", "35.191.0.0/16"]
  target_tags = ["minion"]
}

resource "google_compute_firewall" "allow-internal-all" {
  name = "allow-internal-all"
  network = "${google_compute_network.djchangular-vpc.name}"
  description = "Firewall rule to allow traffic from anywhere on the vpc network to any instances"

  allow {
    protocol = "icmp"
  }

  allow {
    protocol = "tcp"
  }

  source_ranges = ["10.0.0.0/16"]
  target_tags = ["minion", "public", "db"]

}
