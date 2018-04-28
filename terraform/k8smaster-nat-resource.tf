resource "google_compute_instance" "k8smaster-nat-instance" {
  name         = "k8smaster-nat-instance"
  machine_type = "n1-standard-1"
  zone         = "asia-south1-a"
  can_ip_forward = true
  tags = ["public"]
  description = "Linux instance that acts as both the k8s master and the nat gateway"
  boot_disk {
    initialize_params {
      image = "ubuntu-1604-xenial-v20180418"
    }
  }

  network_interface {
    subnetwork = "${google_compute_subnetwork.public-subnetwork.name}"

    access_config {
      nat_ip = "${google_compute_address.lb-nat-address.address}"
    }
  }

  provisioner "file" {
    connection {
      user = "djchangular"
      private_key = "${file(var.gce-ssh-private-key-file)}"
    }

    source      = "/Users/eugene/Desktop/Andela/jsterraform/files/k8s/"
    destination = "/tmp"
  }

  provisioner "remote-exec" {
    connection {
      user = "djchangular"
      private_key = "${file(var.gce-ssh-private-key-file)}"
    }

    inline = [
    ". /tmp/k8smaster-nat.sh; . /tmp/docker.sh"
    ]
  }
}