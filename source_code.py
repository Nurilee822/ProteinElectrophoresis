import sys
from tensorflow import keras
import tensorflow.keras.backend as K
import inspect
import os

file_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(f"{file_path}/layers")
sys.path.append(f"{file_path}/utils")


from base_model import BaseModel
from inspect import getmembers, isfunction

import tensorflow as tf
import layer_60a5c90c82ffc54caedc44d6 as layer_60a5c90c82ffc54caedc44d6
import layer_60a5c90c82ffc54caedc44da as layer_60a5c90c82ffc54caedc44da
import layer_60a5c90c82ffc54caedc44de as layer_60a5c90c82ffc54caedc44de
import layer_60a5c90c82ffc54caedc44dc as layer_60a5c90c82ffc54caedc44dc
import layer_60a5c90c82ffc54caedc44e0 as layer_60a5c90c82ffc54caedc44e0
import layer_60a5c90c82ffc54caedc44e2 as layer_60a5c90c82ffc54caedc44e2
import layer_60a5c90c82ffc54caedc44e4 as layer_60a5c90c82ffc54caedc44e4
import layer_60a5c90c82ffc54caedc44e6 as layer_60a5c90c82ffc54caedc44e6
import layer_60a5c90c82ffc54caedc44e8 as layer_60a5c90c82ffc54caedc44e8
import layer_60a5c90c82ffc54caedc44ea as layer_60a5c90c82ffc54caedc44ea
import layer_60a5c90c82ffc54caedc44ec as layer_60a5c90c82ffc54caedc44ec
import layer_60a5c90c82ffc54caedc452a as layer_60a5c90c82ffc54caedc452a
import layer_60a5c90c82ffc54caedc44f2 as layer_60a5c90c82ffc54caedc44f2
import layer_60a5c90c82ffc54caedc44f6 as layer_60a5c90c82ffc54caedc44f6
import layer_60a5c90c82ffc54caedc44fa as layer_60a5c90c82ffc54caedc44fa
import layer_60a5c90c82ffc54caedc44fe as layer_60a5c90c82ffc54caedc44fe
import layer_60a5c90c82ffc54caedc450a as layer_60a5c90c82ffc54caedc450a
import layer_60a5c90c82ffc54caedc450e as layer_60a5c90c82ffc54caedc450e
import layer_60a5c90c82ffc54caedc4520 as layer_60a5c90c82ffc54caedc4520
import layer_60a5c90c82ffc54caedc4524 as layer_60a5c90c82ffc54caedc4524
import layer_60a5c90c82ffc54caedc4528 as layer_60a5c90c82ffc54caedc4528
import layer_60a5c90c82ffc54caedc44f4 as layer_60a5c90c82ffc54caedc44f4
import layer_60a5c90c82ffc54caedc44fc as layer_60a5c90c82ffc54caedc44fc
import layer_60a5c90c82ffc54caedc4502 as layer_60a5c90c82ffc54caedc4502
import layer_60a5c90c82ffc54caedc4506 as layer_60a5c90c82ffc54caedc4506
import layer_60a5c90c82ffc54caedc450c as layer_60a5c90c82ffc54caedc450c
import layer_60a5c90c82ffc54caedc4512 as layer_60a5c90c82ffc54caedc4512
import layer_60a5c90c82ffc54caedc4516 as layer_60a5c90c82ffc54caedc4516
import layer_60a5c90c82ffc54caedc4526 as layer_60a5c90c82ffc54caedc4526
import layer_60a5c90c82ffc54caedc4504 as layer_60a5c90c82ffc54caedc4504
import layer_60a5c90c82ffc54caedc4514 as layer_60a5c90c82ffc54caedc4514
import layer_60a5c90c82ffc54caedc451a as layer_60a5c90c82ffc54caedc451a
import layer_60a5c90c82ffc54caedc451e as layer_60a5c90c82ffc54caedc451e
import layer_60a5c90c82ffc54caedc451c as layer_60a5c90c82ffc54caedc451c
import layer_60a5c90c82ffc54caedc452f as layer_60a5c90c82ffc54caedc452f
import layer_60a5c90c82ffc54caedc456d as layer_60a5c90c82ffc54caedc456d
import layer_60a5c90c82ffc54caedc4535 as layer_60a5c90c82ffc54caedc4535
import layer_60a5c90c82ffc54caedc4539 as layer_60a5c90c82ffc54caedc4539
import layer_60a5c90c82ffc54caedc453d as layer_60a5c90c82ffc54caedc453d
import layer_60a5c90c82ffc54caedc4541 as layer_60a5c90c82ffc54caedc4541
import layer_60a5c90c82ffc54caedc454d as layer_60a5c90c82ffc54caedc454d
import layer_60a5c90c82ffc54caedc4551 as layer_60a5c90c82ffc54caedc4551
import layer_60a5c90c82ffc54caedc4563 as layer_60a5c90c82ffc54caedc4563
import layer_60a5c90c82ffc54caedc4567 as layer_60a5c90c82ffc54caedc4567
import layer_60a5c90c82ffc54caedc456b as layer_60a5c90c82ffc54caedc456b
import layer_60a5c90c82ffc54caedc4537 as layer_60a5c90c82ffc54caedc4537
import layer_60a5c90c82ffc54caedc453f as layer_60a5c90c82ffc54caedc453f
import layer_60a5c90c82ffc54caedc4545 as layer_60a5c90c82ffc54caedc4545
import layer_60a5c90c82ffc54caedc4549 as layer_60a5c90c82ffc54caedc4549
import layer_60a5c90c82ffc54caedc454f as layer_60a5c90c82ffc54caedc454f
import layer_60a5c90c82ffc54caedc4555 as layer_60a5c90c82ffc54caedc4555
import layer_60a5c90c82ffc54caedc4559 as layer_60a5c90c82ffc54caedc4559
import layer_60a5c90c82ffc54caedc4569 as layer_60a5c90c82ffc54caedc4569
import layer_60a5c90c82ffc54caedc4547 as layer_60a5c90c82ffc54caedc4547
import layer_60a5c90c82ffc54caedc4557 as layer_60a5c90c82ffc54caedc4557
import layer_60a5c90c82ffc54caedc455d as layer_60a5c90c82ffc54caedc455d
import layer_60a5c90c82ffc54caedc4561 as layer_60a5c90c82ffc54caedc4561
import layer_60a5c90c82ffc54caedc455f as layer_60a5c90c82ffc54caedc455f
import layer_60a5c90c82ffc54caedc4572 as layer_60a5c90c82ffc54caedc4572
import layer_60a5c90c82ffc54caedc45b0 as layer_60a5c90c82ffc54caedc45b0
import layer_60a5c90c82ffc54caedc4578 as layer_60a5c90c82ffc54caedc4578
import layer_60a5c90c82ffc54caedc457c as layer_60a5c90c82ffc54caedc457c
import layer_60a5c90c82ffc54caedc4580 as layer_60a5c90c82ffc54caedc4580
import layer_60a5c90c82ffc54caedc4584 as layer_60a5c90c82ffc54caedc4584
import layer_60a5c90c82ffc54caedc4590 as layer_60a5c90c82ffc54caedc4590
import layer_60a5c90c82ffc54caedc4594 as layer_60a5c90c82ffc54caedc4594
import layer_60a5c90c82ffc54caedc45a6 as layer_60a5c90c82ffc54caedc45a6
import layer_60a5c90c82ffc54caedc45aa as layer_60a5c90c82ffc54caedc45aa
import layer_60a5c90c82ffc54caedc45ae as layer_60a5c90c82ffc54caedc45ae
import layer_60a5c90c82ffc54caedc457a as layer_60a5c90c82ffc54caedc457a
import layer_60a5c90c82ffc54caedc4582 as layer_60a5c90c82ffc54caedc4582
import layer_60a5c90c82ffc54caedc4588 as layer_60a5c90c82ffc54caedc4588
import layer_60a5c90c82ffc54caedc458c as layer_60a5c90c82ffc54caedc458c
import layer_60a5c90c82ffc54caedc4592 as layer_60a5c90c82ffc54caedc4592
import layer_60a5c90c82ffc54caedc4598 as layer_60a5c90c82ffc54caedc4598
import layer_60a5c90c82ffc54caedc459c as layer_60a5c90c82ffc54caedc459c
import layer_60a5c90c82ffc54caedc45ac as layer_60a5c90c82ffc54caedc45ac
import layer_60a5c90c82ffc54caedc458a as layer_60a5c90c82ffc54caedc458a
import layer_60a5c90c82ffc54caedc459a as layer_60a5c90c82ffc54caedc459a
import layer_60a5c90c82ffc54caedc45a0 as layer_60a5c90c82ffc54caedc45a0
import layer_60a5c90c82ffc54caedc45a4 as layer_60a5c90c82ffc54caedc45a4
import layer_60a5c90c82ffc54caedc45a2 as layer_60a5c90c82ffc54caedc45a2
import layer_60a5c90c82ffc54caedc45b5 as layer_60a5c90c82ffc54caedc45b5
import layer_60a5c90c82ffc54caedc45c1 as layer_60a5c90c82ffc54caedc45c1
import layer_60a5c90c82ffc54caedc45c5 as layer_60a5c90c82ffc54caedc45c5
import layer_60a5c90c82ffc54caedc45c7 as layer_60a5c90c82ffc54caedc45c7
import layer_60a5c90c82ffc54caedc45c9 as layer_60a5c90c82ffc54caedc45c9
import layer_60a5c90c82ffc54caedc45cd as layer_60a5c90c82ffc54caedc45cd
import layer_60a5c90c82ffc54caedc45cf as layer_60a5c90c82ffc54caedc45cf
import layer_60a5c90c82ffc54caedc45d1 as layer_60a5c90c82ffc54caedc45d1
import layer_60a5c90c82ffc54caedc45d5 as layer_60a5c90c82ffc54caedc45d5
import layer_60a5c90c82ffc54caedc45d7 as layer_60a5c90c82ffc54caedc45d7
import layer_60a5c90c82ffc54caedc45d9 as layer_60a5c90c82ffc54caedc45d9
import layer_60a5c90c82ffc54caedc45db as layer_60a5c90c82ffc54caedc45db
import layer_60a5c90c82ffc54caedc45bb as layer_60a5c90c82ffc54caedc45bb
import layer_60a5c90c82ffc54caedc45bd as layer_60a5c90c82ffc54caedc45bd
import layer_60a5c90c82ffc54caedc45bf as layer_60a5c90c82ffc54caedc45bf
import layer_60a5c90c82ffc54caedc45df as layer_60a5c90c82ffc54caedc45df
import layer_60a5c90c82ffc54caedc4613 as layer_60a5c90c82ffc54caedc4613
import layer_60a5c90c82ffc54caedc45e5 as layer_60a5c90c82ffc54caedc45e5
import layer_60a5c90c82ffc54caedc45e9 as layer_60a5c90c82ffc54caedc45e9
import layer_60a5c90c82ffc54caedc45ed as layer_60a5c90c82ffc54caedc45ed
import layer_60a5c90c82ffc54caedc45f1 as layer_60a5c90c82ffc54caedc45f1
import layer_60a5c90c82ffc54caedc4603 as layer_60a5c90c82ffc54caedc4603
import layer_60a5c90c82ffc54caedc4607 as layer_60a5c90c82ffc54caedc4607
import layer_60a5c90c82ffc54caedc4609 as layer_60a5c90c82ffc54caedc4609
import layer_60a5c90c82ffc54caedc460d as layer_60a5c90c82ffc54caedc460d
import layer_60a5c90c82ffc54caedc4611 as layer_60a5c90c82ffc54caedc4611
import layer_60a5c90c82ffc54caedc45e7 as layer_60a5c90c82ffc54caedc45e7
import layer_60a5c90c82ffc54caedc45ef as layer_60a5c90c82ffc54caedc45ef
import layer_60a5c90c82ffc54caedc45f5 as layer_60a5c90c82ffc54caedc45f5
import layer_60a5c90c82ffc54caedc45f9 as layer_60a5c90c82ffc54caedc45f9
import layer_60a5c90c82ffc54caedc4605 as layer_60a5c90c82ffc54caedc4605
import layer_60a5c90c82ffc54caedc460f as layer_60a5c90c82ffc54caedc460f
import layer_60a5c90c82ffc54caedc461c as layer_60a5c90c82ffc54caedc461c
import layer_60a5c90c82ffc54caedc4620 as layer_60a5c90c82ffc54caedc4620
import layer_60a5c90c82ffc54caedc45f7 as layer_60a5c90c82ffc54caedc45f7
import layer_60a5c90c82ffc54caedc45fb as layer_60a5c90c82ffc54caedc45fb
import layer_60a5c90c82ffc54caedc45fd as layer_60a5c90c82ffc54caedc45fd
import layer_60a5c90c82ffc54caedc45ff as layer_60a5c90c82ffc54caedc45ff
import layer_60a5c90c82ffc54caedc461e as layer_60a5c90c82ffc54caedc461e
import layer_60a5c90c82ffc54caedc4622 as layer_60a5c90c82ffc54caedc4622
import layer_60a5c90c82ffc54caedc4624 as layer_60a5c90c82ffc54caedc4624
import layer_60a5c90c82ffc54caedc4626 as layer_60a5c90c82ffc54caedc4626
import layer_60a5c90c82ffc54caedc462a as layer_60a5c90c82ffc54caedc462a
import layer_60a5c90c82ffc54caedc462e as layer_60a5c90c82ffc54caedc462e
import layer_60a5c90c82ffc54caedc462c as layer_60a5c90c82ffc54caedc462c
import layer_60a5c90c82ffc54caedc4630 as layer_60a5c90c82ffc54caedc4630
import layer_60a5c90c82ffc54caedc4632 as layer_60a5c90c82ffc54caedc4632
import layer_60a5c90c82ffc54caedc4634 as layer_60a5c90c82ffc54caedc4634
import layer_60a5c90c82ffc54caedc4618 as layer_60a5c90c82ffc54caedc4618
import layer_60a5c90c82ffc54caedc4668 as layer_60a5c90c82ffc54caedc4668
import layer_60a5c90c82ffc54caedc463a as layer_60a5c90c82ffc54caedc463a
import layer_60a5c90c82ffc54caedc463e as layer_60a5c90c82ffc54caedc463e
import layer_60a5c90c82ffc54caedc4642 as layer_60a5c90c82ffc54caedc4642
import layer_60a5c90c82ffc54caedc4646 as layer_60a5c90c82ffc54caedc4646
import layer_60a5c90c82ffc54caedc4658 as layer_60a5c90c82ffc54caedc4658
import layer_60a5c90c82ffc54caedc465c as layer_60a5c90c82ffc54caedc465c
import layer_60a5c90c82ffc54caedc465e as layer_60a5c90c82ffc54caedc465e
import layer_60a5c90c82ffc54caedc4662 as layer_60a5c90c82ffc54caedc4662
import layer_60a5c90c82ffc54caedc4666 as layer_60a5c90c82ffc54caedc4666
import layer_60a5c90c82ffc54caedc463c as layer_60a5c90c82ffc54caedc463c
import layer_60a5c90c82ffc54caedc4644 as layer_60a5c90c82ffc54caedc4644
import layer_60a5c90c82ffc54caedc464a as layer_60a5c90c82ffc54caedc464a
import layer_60a5c90c82ffc54caedc464e as layer_60a5c90c82ffc54caedc464e
import layer_60a5c90c82ffc54caedc465a as layer_60a5c90c82ffc54caedc465a
import layer_60a5c90c82ffc54caedc4664 as layer_60a5c90c82ffc54caedc4664
import layer_60a5c90c82ffc54caedc4671 as layer_60a5c90c82ffc54caedc4671
import layer_60a5c90c82ffc54caedc4675 as layer_60a5c90c82ffc54caedc4675
import layer_60a5c90c82ffc54caedc464c as layer_60a5c90c82ffc54caedc464c
import layer_60a5c90c82ffc54caedc4650 as layer_60a5c90c82ffc54caedc4650
import layer_60a5c90c82ffc54caedc4652 as layer_60a5c90c82ffc54caedc4652
import layer_60a5c90c82ffc54caedc4654 as layer_60a5c90c82ffc54caedc4654
import layer_60a5c90c82ffc54caedc4673 as layer_60a5c90c82ffc54caedc4673
import layer_60a5c90c82ffc54caedc4677 as layer_60a5c90c82ffc54caedc4677
import layer_60a5c90c82ffc54caedc4679 as layer_60a5c90c82ffc54caedc4679
import layer_60a5c90c82ffc54caedc467b as layer_60a5c90c82ffc54caedc467b
import layer_60a5c90c82ffc54caedc467f as layer_60a5c90c82ffc54caedc467f
import layer_60a5c90c82ffc54caedc4683 as layer_60a5c90c82ffc54caedc4683
import layer_60a5c90c82ffc54caedc4681 as layer_60a5c90c82ffc54caedc4681
import layer_60a5c90c82ffc54caedc4685 as layer_60a5c90c82ffc54caedc4685
import layer_60a5c90c82ffc54caedc4687 as layer_60a5c90c82ffc54caedc4687
import layer_60a5c90c82ffc54caedc4689 as layer_60a5c90c82ffc54caedc4689
import layer_60a5c90c82ffc54caedc466d as layer_60a5c90c82ffc54caedc466d
import layer_60a5c90c82ffc54caedc4712 as layer_60a5c90c82ffc54caedc4712
import layer_60a5c90c82ffc54caedc46e4 as layer_60a5c90c82ffc54caedc46e4
import layer_60a5c90c82ffc54caedc46e8 as layer_60a5c90c82ffc54caedc46e8
import layer_60a5c90c82ffc54caedc46ec as layer_60a5c90c82ffc54caedc46ec
import layer_60a5c90c82ffc54caedc46f0 as layer_60a5c90c82ffc54caedc46f0
import layer_60a5c90c82ffc54caedc4702 as layer_60a5c90c82ffc54caedc4702
import layer_60a5c90c82ffc54caedc4706 as layer_60a5c90c82ffc54caedc4706
import layer_60a5c90c82ffc54caedc4708 as layer_60a5c90c82ffc54caedc4708
import layer_60a5c90c82ffc54caedc470c as layer_60a5c90c82ffc54caedc470c
import layer_60a5c90c82ffc54caedc4710 as layer_60a5c90c82ffc54caedc4710
import layer_60a5c90c82ffc54caedc46e6 as layer_60a5c90c82ffc54caedc46e6
import layer_60a5c90c82ffc54caedc46ee as layer_60a5c90c82ffc54caedc46ee
import layer_60a5c90c82ffc54caedc46f4 as layer_60a5c90c82ffc54caedc46f4
import layer_60a5c90c82ffc54caedc46f8 as layer_60a5c90c82ffc54caedc46f8
import layer_60a5c90c82ffc54caedc4704 as layer_60a5c90c82ffc54caedc4704
import layer_60a5c90c82ffc54caedc470e as layer_60a5c90c82ffc54caedc470e
import layer_60a5c90c82ffc54caedc471b as layer_60a5c90c82ffc54caedc471b
import layer_60a5c90c82ffc54caedc471f as layer_60a5c90c82ffc54caedc471f
import layer_60a5c90c82ffc54caedc46f6 as layer_60a5c90c82ffc54caedc46f6
import layer_60a5c90c82ffc54caedc46fa as layer_60a5c90c82ffc54caedc46fa
import layer_60a5c90c82ffc54caedc46fc as layer_60a5c90c82ffc54caedc46fc
import layer_60a5c90c82ffc54caedc46fe as layer_60a5c90c82ffc54caedc46fe
import layer_60a5c90c82ffc54caedc471d as layer_60a5c90c82ffc54caedc471d
import layer_60a5c90c82ffc54caedc4721 as layer_60a5c90c82ffc54caedc4721
import layer_60a5c90c82ffc54caedc4723 as layer_60a5c90c82ffc54caedc4723
import layer_60a5c90c82ffc54caedc4725 as layer_60a5c90c82ffc54caedc4725
import layer_60a5c90c82ffc54caedc4729 as layer_60a5c90c82ffc54caedc4729
import layer_60a5c90c82ffc54caedc472d as layer_60a5c90c82ffc54caedc472d
import layer_60a5c90c82ffc54caedc472b as layer_60a5c90c82ffc54caedc472b
import layer_60a5c90c82ffc54caedc472f as layer_60a5c90c82ffc54caedc472f
import layer_60a5c90c82ffc54caedc4731 as layer_60a5c90c82ffc54caedc4731
import layer_60a5c90c82ffc54caedc4733 as layer_60a5c90c82ffc54caedc4733
import layer_60a5c90c82ffc54caedc4717 as layer_60a5c90c82ffc54caedc4717
import layer_60a5c90c82ffc54caedc46bd as layer_60a5c90c82ffc54caedc46bd
import layer_60a5c90c82ffc54caedc468f as layer_60a5c90c82ffc54caedc468f
import layer_60a5c90c82ffc54caedc4693 as layer_60a5c90c82ffc54caedc4693
import layer_60a5c90c82ffc54caedc4697 as layer_60a5c90c82ffc54caedc4697
import layer_60a5c90c82ffc54caedc469b as layer_60a5c90c82ffc54caedc469b
import layer_60a5c90c82ffc54caedc46ad as layer_60a5c90c82ffc54caedc46ad
import layer_60a5c90c82ffc54caedc46b1 as layer_60a5c90c82ffc54caedc46b1
import layer_60a5c90c82ffc54caedc46b3 as layer_60a5c90c82ffc54caedc46b3
import layer_60a5c90c82ffc54caedc46b7 as layer_60a5c90c82ffc54caedc46b7
import layer_60a5c90c82ffc54caedc46bb as layer_60a5c90c82ffc54caedc46bb
import layer_60a5c90c82ffc54caedc4691 as layer_60a5c90c82ffc54caedc4691
import layer_60a5c90c82ffc54caedc4699 as layer_60a5c90c82ffc54caedc4699
import layer_60a5c90c82ffc54caedc469f as layer_60a5c90c82ffc54caedc469f
import layer_60a5c90c82ffc54caedc46a3 as layer_60a5c90c82ffc54caedc46a3
import layer_60a5c90c82ffc54caedc46af as layer_60a5c90c82ffc54caedc46af
import layer_60a5c90c82ffc54caedc46b9 as layer_60a5c90c82ffc54caedc46b9
import layer_60a5c90c82ffc54caedc46c6 as layer_60a5c90c82ffc54caedc46c6
import layer_60a5c90c82ffc54caedc46ca as layer_60a5c90c82ffc54caedc46ca
import layer_60a5c90c82ffc54caedc46a1 as layer_60a5c90c82ffc54caedc46a1
import layer_60a5c90c82ffc54caedc46a5 as layer_60a5c90c82ffc54caedc46a5
import layer_60a5c90c82ffc54caedc46a7 as layer_60a5c90c82ffc54caedc46a7
import layer_60a5c90c82ffc54caedc46a9 as layer_60a5c90c82ffc54caedc46a9
import layer_60a5c90c82ffc54caedc46c8 as layer_60a5c90c82ffc54caedc46c8
import layer_60a5c90c82ffc54caedc46cc as layer_60a5c90c82ffc54caedc46cc
import layer_60a5c90c82ffc54caedc46ce as layer_60a5c90c82ffc54caedc46ce
import layer_60a5c90c82ffc54caedc46d0 as layer_60a5c90c82ffc54caedc46d0
import layer_60a5c90c82ffc54caedc46d4 as layer_60a5c90c82ffc54caedc46d4
import layer_60a5c90c82ffc54caedc46d8 as layer_60a5c90c82ffc54caedc46d8
import layer_60a5c90c82ffc54caedc46d6 as layer_60a5c90c82ffc54caedc46d6
import layer_60a5c90c82ffc54caedc46da as layer_60a5c90c82ffc54caedc46da
import layer_60a5c90c82ffc54caedc46dc as layer_60a5c90c82ffc54caedc46dc
import layer_60a5c90c82ffc54caedc46de as layer_60a5c90c82ffc54caedc46de
import layer_60a5c90c82ffc54caedc46c2 as layer_60a5c90c82ffc54caedc46c2
import layer_60a5c90c82ffc54caedc473f as layer_60a5c90c82ffc54caedc473f
import layer_60a5c90c82ffc54caedc4743 as layer_60a5c90c82ffc54caedc4743
import layer_60a5c90c82ffc54caedc4745 as layer_60a5c90c82ffc54caedc4745
import layer_60a5c90c82ffc54caedc4747 as layer_60a5c90c82ffc54caedc4747
import layer_60a5c90c82ffc54caedc474b as layer_60a5c90c82ffc54caedc474b
import layer_60a5c90c82ffc54caedc474d as layer_60a5c90c82ffc54caedc474d
import layer_60a5c90c82ffc54caedc474f as layer_60a5c90c82ffc54caedc474f
import layer_60a5c90c82ffc54caedc4751 as layer_60a5c90c82ffc54caedc4751
import layer_60a5c90c82ffc54caedc4753 as layer_60a5c90c82ffc54caedc4753
import layer_60a5c90c82ffc54caedc4755 as layer_60a5c90c82ffc54caedc4755
import layer_60a5c90c82ffc54caedc4759 as layer_60a5c90c82ffc54caedc4759
import layer_60a5c90c82ffc54caedc475b as layer_60a5c90c82ffc54caedc475b
import layer_60a5c90c82ffc54caedc475d as layer_60a5c90c82ffc54caedc475d
import layer_60a5c90c82ffc54caedc475f as layer_60a5c90c82ffc54caedc475f
import layer_60a5c90c82ffc54caedc4739 as layer_60a5c90c82ffc54caedc4739
import layer_60a5c90c82ffc54caedc473b as layer_60a5c90c82ffc54caedc473b
import layer_60a5c90c82ffc54caedc473d as layer_60a5c90c82ffc54caedc473d
import layer_60a5c90c82ffc54caedc4767 as layer_60a5c90c82ffc54caedc4767
import layer_60a5c90c82ffc54caedc4769 as layer_60a5c90c82ffc54caedc4769
import layer_60a5c90c82ffc54caedc476b as layer_60a5c90c82ffc54caedc476b
import layer_60a5c90c82ffc54caedc4763 as layer_60a5c90c82ffc54caedc4763
import layer_60a5c90c82ffc54caedc4777 as layer_60a5c90c82ffc54caedc4777
import layer_60a5c90c82ffc54caedc477b as layer_60a5c90c82ffc54caedc477b
import layer_60a5c90c82ffc54caedc477d as layer_60a5c90c82ffc54caedc477d
import layer_60a5c90c82ffc54caedc477f as layer_60a5c90c82ffc54caedc477f
import layer_60a5c90c82ffc54caedc4783 as layer_60a5c90c82ffc54caedc4783
import layer_60a5c90c82ffc54caedc4785 as layer_60a5c90c82ffc54caedc4785
import layer_60a5c90c82ffc54caedc4787 as layer_60a5c90c82ffc54caedc4787
import layer_60a5c90c82ffc54caedc478b as layer_60a5c90c82ffc54caedc478b
import layer_60a5c90c82ffc54caedc478d as layer_60a5c90c82ffc54caedc478d
import layer_60a5c90c82ffc54caedc478f as layer_60a5c90c82ffc54caedc478f
import layer_60a5c90c82ffc54caedc4792 as layer_60a5c90c82ffc54caedc4792
import layer_60a5c90c82ffc54caedc4796 as layer_60a5c90c82ffc54caedc4796
import layer_60a5c90c82ffc54caedc4798 as layer_60a5c90c82ffc54caedc4798
import layer_60a5c90c82ffc54caedc479a as layer_60a5c90c82ffc54caedc479a
import layer_60a5c90c82ffc54caedc479e as layer_60a5c90c82ffc54caedc479e
import layer_60a5c90c82ffc54caedc47a0 as layer_60a5c90c82ffc54caedc47a0
import layer_60a5c90c82ffc54caedc47a2 as layer_60a5c90c82ffc54caedc47a2
import layer_60a5c90c82ffc54caedc47a6 as layer_60a5c90c82ffc54caedc47a6
import layer_60a5c90c82ffc54caedc47a8 as layer_60a5c90c82ffc54caedc47a8
import layer_60a5c90c82ffc54caedc47aa as layer_60a5c90c82ffc54caedc47aa
import layer_60a5c90c82ffc54caedc47ae as layer_60a5c90c82ffc54caedc47ae
import layer_60a5c90c82ffc54caedc47b0 as layer_60a5c90c82ffc54caedc47b0
import layer_60a5c90c82ffc54caedc47b2 as layer_60a5c90c82ffc54caedc47b2
import layer_60a5c90c82ffc54caedc47b5 as layer_60a5c90c82ffc54caedc47b5
import layer_60a5c90c82ffc54caedc47b7 as layer_60a5c90c82ffc54caedc47b7
import layer_60a5c90c82ffc54caedc47bb as layer_60a5c90c82ffc54caedc47bb
import layer_60a5c90c82ffc54caedc47bd as layer_60a5c90c82ffc54caedc47bd
import layer_60a5c90c82ffc54caedc47bf as layer_60a5c90c82ffc54caedc47bf
import layer_60a5c90c82ffc54caedc4771 as layer_60a5c90c82ffc54caedc4771
import layer_60a5c90c82ffc54caedc4773 as layer_60a5c90c82ffc54caedc4773
import layer_60a5c90c82ffc54caedc4775 as layer_60a5c90c82ffc54caedc4775
import layer_60a5c90c82ffc54caedc47c4 as layer_60a5c90c82ffc54caedc47c4
import layer_60a5c90c82ffc54caedc47d0 as layer_60a5c90c82ffc54caedc47d0
import layer_60a5c90c82ffc54caedc47d4 as layer_60a5c90c82ffc54caedc47d4
import layer_60a5c90c82ffc54caedc47d6 as layer_60a5c90c82ffc54caedc47d6
import layer_60a5c90c82ffc54caedc47d8 as layer_60a5c90c82ffc54caedc47d8
import layer_60a5c90c82ffc54caedc47dc as layer_60a5c90c82ffc54caedc47dc
import layer_60a5c90c82ffc54caedc47de as layer_60a5c90c82ffc54caedc47de
import layer_60a5c90c82ffc54caedc47e0 as layer_60a5c90c82ffc54caedc47e0
import layer_60a5c90c82ffc54caedc47e4 as layer_60a5c90c82ffc54caedc47e4
import layer_60a5c90c82ffc54caedc47e6 as layer_60a5c90c82ffc54caedc47e6
import layer_60a5c90c82ffc54caedc47e8 as layer_60a5c90c82ffc54caedc47e8
import layer_60a5c90c82ffc54caedc47eb as layer_60a5c90c82ffc54caedc47eb
import layer_60a5c90c82ffc54caedc47ef as layer_60a5c90c82ffc54caedc47ef
import layer_60a5c90c82ffc54caedc47f1 as layer_60a5c90c82ffc54caedc47f1
import layer_60a5c90c82ffc54caedc47f3 as layer_60a5c90c82ffc54caedc47f3
import layer_60a5c90c82ffc54caedc47f7 as layer_60a5c90c82ffc54caedc47f7
import layer_60a5c90c82ffc54caedc47f9 as layer_60a5c90c82ffc54caedc47f9
import layer_60a5c90c82ffc54caedc47fb as layer_60a5c90c82ffc54caedc47fb
import layer_60a5c90c82ffc54caedc47ff as layer_60a5c90c82ffc54caedc47ff
import layer_60a5c90c82ffc54caedc4801 as layer_60a5c90c82ffc54caedc4801
import layer_60a5c90c82ffc54caedc4803 as layer_60a5c90c82ffc54caedc4803
import layer_60a5c90c82ffc54caedc4807 as layer_60a5c90c82ffc54caedc4807
import layer_60a5c90c82ffc54caedc4809 as layer_60a5c90c82ffc54caedc4809
import layer_60a5c90c82ffc54caedc480b as layer_60a5c90c82ffc54caedc480b
import layer_60a5c90c82ffc54caedc480e as layer_60a5c90c82ffc54caedc480e
import layer_60a5c90c82ffc54caedc4810 as layer_60a5c90c82ffc54caedc4810
import layer_60a5c90c82ffc54caedc4814 as layer_60a5c90c82ffc54caedc4814
import layer_60a5c90c82ffc54caedc4816 as layer_60a5c90c82ffc54caedc4816
import layer_60a5c90c82ffc54caedc4818 as layer_60a5c90c82ffc54caedc4818
import layer_60a5c90c82ffc54caedc47ca as layer_60a5c90c82ffc54caedc47ca
import layer_60a5c90c82ffc54caedc47cc as layer_60a5c90c82ffc54caedc47cc
import layer_60a5c90c82ffc54caedc47ce as layer_60a5c90c82ffc54caedc47ce
import layer_60a5c90c82ffc54caedc481d as layer_60a5c90c82ffc54caedc481d
import layer_60a5c90c82ffc54caedc481f as layer_60a5c90c82ffc54caedc481f
import layer_60a5c90c82ffc54caedc4823 as layer_60a5c90c82ffc54caedc4823
import layer_60a5c90c82ffc54caedc4821 as layer_60a5c90c82ffc54caedc4821


def get_layer_object(module):
    for member in getmembers(module):
        if member[1].__module__ == module.__name__:
            return member[1]

def get_loss_sum_fn(list_loss):
    def LossSum(y_true, y_pred):
        loss = 0
        for loss_fn in list_loss:
            loss += loss_fn(y_true, y_pred)
        return loss

    return LossSum

class Model(BaseModel):
    def __init__(self, *args, **kwargs):
        super(Model, self).__init__(*args, **kwargs)
        self.path_weight = file_path + "/weight.hdf5"
        inputs, outputs, losses, labels = self.build_source()
        self.compile(inputs, outputs, losses, labels)

    def build_source(self):
        config_loss = dict()
        volume = 256
        height = 256
        width = 256
        channels = 1
        num_class = 6
        output_channels = 1
        batch_size = 1

        n1_Image = layer_60a5c90c82ffc54caedc44d6.Image(shape=[256, 256, 1])
        n2_Backbone_n1_Conv2D = layer_60a5c90c82ffc54caedc44da.Conv2D(filters=32, kernel_size=[3, 3], strides=[2, 2], padding='valid', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n1_Image)
        n2_Backbone_n3_BatchNormalization = layer_60a5c90c82ffc54caedc44de.BatchNormalization()(n2_Backbone_n1_Conv2D)
        n2_Backbone_n2_Activation = layer_60a5c90c82ffc54caedc44dc.Activation(activation='relu')(n2_Backbone_n3_BatchNormalization)
        n2_Backbone_n4_Conv2D = layer_60a5c90c82ffc54caedc44e0.Conv2D(filters=32, kernel_size=[3, 3], strides=[1, 1], padding='valid', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n2_Activation)
        n2_Backbone_n5_BatchNormalization = layer_60a5c90c82ffc54caedc44e2.BatchNormalization()(n2_Backbone_n4_Conv2D)
        n2_Backbone_n6_Activation = layer_60a5c90c82ffc54caedc44e4.Activation(activation='relu')(n2_Backbone_n5_BatchNormalization)
        n2_Backbone_n7_Conv2D = layer_60a5c90c82ffc54caedc44e6.Conv2D(filters=64, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n6_Activation)
        n2_Backbone_n8_BatchNormalization = layer_60a5c90c82ffc54caedc44e8.BatchNormalization()(n2_Backbone_n7_Conv2D)
        n2_Backbone_n9_Activation = layer_60a5c90c82ffc54caedc44ea.Activation(activation='relu')(n2_Backbone_n8_BatchNormalization)
        n2_Backbone_n10_MaxPooling2D = layer_60a5c90c82ffc54caedc44ec.MaxPooling2D(pool_size=[2, 2], strides=[2, 2], padding='valid')(n2_Backbone_n9_Activation)
        n2_Backbone_n11_mixed_0_n9_Activation = layer_60a5c90c82ffc54caedc452a.Activation(activation='linear')(n2_Backbone_n10_MaxPooling2D)
        n2_Backbone_n11_mixed_0_n1_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc44f2.Conv2D(filters=64, kernel_size=[1, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n11_mixed_0_n9_Activation)
        n2_Backbone_n11_mixed_0_n1_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc44f6.BatchNormalization()(n2_Backbone_n11_mixed_0_n1_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n11_mixed_0_n2_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc44fa.Conv2D(filters=48, kernel_size=[1, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n11_mixed_0_n9_Activation)
        n2_Backbone_n11_mixed_0_n2_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc44fe.BatchNormalization()(n2_Backbone_n11_mixed_0_n2_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n11_mixed_0_n4_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc450a.Conv2D(filters=64, kernel_size=[1, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n11_mixed_0_n9_Activation)
        n2_Backbone_n11_mixed_0_n4_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc450e.BatchNormalization()(n2_Backbone_n11_mixed_0_n4_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n11_mixed_0_n7_AveragePooling2D = layer_60a5c90c82ffc54caedc4520.AveragePooling2D(pool_size=[3, 3], strides=[1, 1], padding='same')(n2_Backbone_n11_mixed_0_n9_Activation)
        n2_Backbone_n11_mixed_0_n8_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc4524.Conv2D(filters=32, kernel_size=[1, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n11_mixed_0_n7_AveragePooling2D)
        n2_Backbone_n11_mixed_0_n8_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc4528.BatchNormalization()(n2_Backbone_n11_mixed_0_n8_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n11_mixed_0_n1_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc44f4.Activation(activation='relu')(n2_Backbone_n11_mixed_0_n1_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n11_mixed_0_n2_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc44fc.Activation(activation='relu')(n2_Backbone_n11_mixed_0_n2_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n11_mixed_0_n3_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc4502.Conv2D(filters=64, kernel_size=[5, 5], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n11_mixed_0_n2_Conv2D_BN_n2_Activation)
        n2_Backbone_n11_mixed_0_n3_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc4506.BatchNormalization()(n2_Backbone_n11_mixed_0_n3_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n11_mixed_0_n4_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc450c.Activation(activation='relu')(n2_Backbone_n11_mixed_0_n4_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n11_mixed_0_n5_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc4512.Conv2D(filters=96, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n11_mixed_0_n4_Conv2D_BN_n2_Activation)
        n2_Backbone_n11_mixed_0_n5_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc4516.BatchNormalization()(n2_Backbone_n11_mixed_0_n5_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n11_mixed_0_n8_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc4526.Activation(activation='relu')(n2_Backbone_n11_mixed_0_n8_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n11_mixed_0_n3_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc4504.Activation(activation='relu')(n2_Backbone_n11_mixed_0_n3_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n11_mixed_0_n5_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc4514.Activation(activation='relu')(n2_Backbone_n11_mixed_0_n5_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n11_mixed_0_n6_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc451a.Conv2D(filters=96, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n11_mixed_0_n5_Conv2D_BN_n2_Activation)
        n2_Backbone_n11_mixed_0_n6_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc451e.BatchNormalization()(n2_Backbone_n11_mixed_0_n6_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n11_mixed_0_n6_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc451c.Activation(activation='relu')(n2_Backbone_n11_mixed_0_n6_Conv2D_BN_n3_BatchNormalization)
        num_args = len(inspect.getfullargspec(layer_60a5c90c82ffc54caedc452f.Concatenate(axis=-1).call).args)
        if num_args == 2:
            n2_Backbone_n11_mixed_0_n10_Concatenate = layer_60a5c90c82ffc54caedc452f.Concatenate(axis=-1)([n2_Backbone_n11_mixed_0_n1_Conv2D_BN_n2_Activation, n2_Backbone_n11_mixed_0_n3_Conv2D_BN_n2_Activation, n2_Backbone_n11_mixed_0_n6_Conv2D_BN_n2_Activation, n2_Backbone_n11_mixed_0_n8_Conv2D_BN_n2_Activation])
        else:
            n2_Backbone_n11_mixed_0_n10_Concatenate = layer_60a5c90c82ffc54caedc452f.Concatenate(axis=-1)(*[n2_Backbone_n11_mixed_0_n1_Conv2D_BN_n2_Activation, n2_Backbone_n11_mixed_0_n3_Conv2D_BN_n2_Activation, n2_Backbone_n11_mixed_0_n6_Conv2D_BN_n2_Activation, n2_Backbone_n11_mixed_0_n8_Conv2D_BN_n2_Activation])
        n2_Backbone_n12_mixed_0_n9_Activation = layer_60a5c90c82ffc54caedc456d.Activation(activation='linear')(n2_Backbone_n11_mixed_0_n10_Concatenate)
        n2_Backbone_n12_mixed_0_n1_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc4535.Conv2D(filters=64, kernel_size=[1, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n12_mixed_0_n9_Activation)
        n2_Backbone_n12_mixed_0_n1_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc4539.BatchNormalization()(n2_Backbone_n12_mixed_0_n1_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n12_mixed_0_n2_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc453d.Conv2D(filters=48, kernel_size=[1, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n12_mixed_0_n9_Activation)
        n2_Backbone_n12_mixed_0_n2_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc4541.BatchNormalization()(n2_Backbone_n12_mixed_0_n2_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n12_mixed_0_n4_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc454d.Conv2D(filters=64, kernel_size=[1, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n12_mixed_0_n9_Activation)
        n2_Backbone_n12_mixed_0_n4_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc4551.BatchNormalization()(n2_Backbone_n12_mixed_0_n4_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n12_mixed_0_n7_AveragePooling2D = layer_60a5c90c82ffc54caedc4563.AveragePooling2D(pool_size=[3, 3], strides=[1, 1], padding='same')(n2_Backbone_n12_mixed_0_n9_Activation)
        n2_Backbone_n12_mixed_0_n8_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc4567.Conv2D(filters=64, kernel_size=[1, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n12_mixed_0_n7_AveragePooling2D)
        n2_Backbone_n12_mixed_0_n8_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc456b.BatchNormalization()(n2_Backbone_n12_mixed_0_n8_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n12_mixed_0_n1_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc4537.Activation(activation='relu')(n2_Backbone_n12_mixed_0_n1_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n12_mixed_0_n2_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc453f.Activation(activation='relu')(n2_Backbone_n12_mixed_0_n2_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n12_mixed_0_n3_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc4545.Conv2D(filters=64, kernel_size=[5, 5], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n12_mixed_0_n2_Conv2D_BN_n2_Activation)
        n2_Backbone_n12_mixed_0_n3_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc4549.BatchNormalization()(n2_Backbone_n12_mixed_0_n3_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n12_mixed_0_n4_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc454f.Activation(activation='relu')(n2_Backbone_n12_mixed_0_n4_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n12_mixed_0_n5_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc4555.Conv2D(filters=96, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n12_mixed_0_n4_Conv2D_BN_n2_Activation)
        n2_Backbone_n12_mixed_0_n5_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc4559.BatchNormalization()(n2_Backbone_n12_mixed_0_n5_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n12_mixed_0_n8_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc4569.Activation(activation='relu')(n2_Backbone_n12_mixed_0_n8_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n12_mixed_0_n3_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc4547.Activation(activation='relu')(n2_Backbone_n12_mixed_0_n3_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n12_mixed_0_n5_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc4557.Activation(activation='relu')(n2_Backbone_n12_mixed_0_n5_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n12_mixed_0_n6_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc455d.Conv2D(filters=96, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n12_mixed_0_n5_Conv2D_BN_n2_Activation)
        n2_Backbone_n12_mixed_0_n6_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc4561.BatchNormalization()(n2_Backbone_n12_mixed_0_n6_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n12_mixed_0_n6_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc455f.Activation(activation='relu')(n2_Backbone_n12_mixed_0_n6_Conv2D_BN_n3_BatchNormalization)
        num_args = len(inspect.getfullargspec(layer_60a5c90c82ffc54caedc4572.Concatenate(axis=-1).call).args)
        if num_args == 2:
            n2_Backbone_n12_mixed_0_n10_Concatenate = layer_60a5c90c82ffc54caedc4572.Concatenate(axis=-1)([n2_Backbone_n12_mixed_0_n1_Conv2D_BN_n2_Activation, n2_Backbone_n12_mixed_0_n3_Conv2D_BN_n2_Activation, n2_Backbone_n12_mixed_0_n6_Conv2D_BN_n2_Activation, n2_Backbone_n12_mixed_0_n8_Conv2D_BN_n2_Activation])
        else:
            n2_Backbone_n12_mixed_0_n10_Concatenate = layer_60a5c90c82ffc54caedc4572.Concatenate(axis=-1)(*[n2_Backbone_n12_mixed_0_n1_Conv2D_BN_n2_Activation, n2_Backbone_n12_mixed_0_n3_Conv2D_BN_n2_Activation, n2_Backbone_n12_mixed_0_n6_Conv2D_BN_n2_Activation, n2_Backbone_n12_mixed_0_n8_Conv2D_BN_n2_Activation])
        n2_Backbone_n13_mixed_0_n9_Activation = layer_60a5c90c82ffc54caedc45b0.Activation(activation='linear')(n2_Backbone_n12_mixed_0_n10_Concatenate)
        n2_Backbone_n13_mixed_0_n1_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc4578.Conv2D(filters=64, kernel_size=[1, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n13_mixed_0_n9_Activation)
        n2_Backbone_n13_mixed_0_n1_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc457c.BatchNormalization()(n2_Backbone_n13_mixed_0_n1_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n13_mixed_0_n2_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc4580.Conv2D(filters=48, kernel_size=[1, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n13_mixed_0_n9_Activation)
        n2_Backbone_n13_mixed_0_n2_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc4584.BatchNormalization()(n2_Backbone_n13_mixed_0_n2_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n13_mixed_0_n4_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc4590.Conv2D(filters=64, kernel_size=[1, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n13_mixed_0_n9_Activation)
        n2_Backbone_n13_mixed_0_n4_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc4594.BatchNormalization()(n2_Backbone_n13_mixed_0_n4_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n13_mixed_0_n7_AveragePooling2D = layer_60a5c90c82ffc54caedc45a6.AveragePooling2D(pool_size=[3, 3], strides=[1, 1], padding='same')(n2_Backbone_n13_mixed_0_n9_Activation)
        n2_Backbone_n13_mixed_0_n8_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc45aa.Conv2D(filters=64, kernel_size=[1, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n13_mixed_0_n7_AveragePooling2D)
        n2_Backbone_n13_mixed_0_n8_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc45ae.BatchNormalization()(n2_Backbone_n13_mixed_0_n8_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n13_mixed_0_n1_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc457a.Activation(activation='relu')(n2_Backbone_n13_mixed_0_n1_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n13_mixed_0_n2_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc4582.Activation(activation='relu')(n2_Backbone_n13_mixed_0_n2_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n13_mixed_0_n3_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc4588.Conv2D(filters=64, kernel_size=[5, 5], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n13_mixed_0_n2_Conv2D_BN_n2_Activation)
        n2_Backbone_n13_mixed_0_n3_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc458c.BatchNormalization()(n2_Backbone_n13_mixed_0_n3_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n13_mixed_0_n4_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc4592.Activation(activation='relu')(n2_Backbone_n13_mixed_0_n4_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n13_mixed_0_n5_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc4598.Conv2D(filters=96, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n13_mixed_0_n4_Conv2D_BN_n2_Activation)
        n2_Backbone_n13_mixed_0_n5_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc459c.BatchNormalization()(n2_Backbone_n13_mixed_0_n5_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n13_mixed_0_n8_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc45ac.Activation(activation='relu')(n2_Backbone_n13_mixed_0_n8_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n13_mixed_0_n3_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc458a.Activation(activation='relu')(n2_Backbone_n13_mixed_0_n3_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n13_mixed_0_n5_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc459a.Activation(activation='relu')(n2_Backbone_n13_mixed_0_n5_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n13_mixed_0_n6_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc45a0.Conv2D(filters=96, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n13_mixed_0_n5_Conv2D_BN_n2_Activation)
        n2_Backbone_n13_mixed_0_n6_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc45a4.BatchNormalization()(n2_Backbone_n13_mixed_0_n6_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n13_mixed_0_n6_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc45a2.Activation(activation='relu')(n2_Backbone_n13_mixed_0_n6_Conv2D_BN_n3_BatchNormalization)
        num_args = len(inspect.getfullargspec(layer_60a5c90c82ffc54caedc45b5.Concatenate(axis=-1).call).args)
        if num_args == 2:
            n2_Backbone_n13_mixed_0_n10_Concatenate = layer_60a5c90c82ffc54caedc45b5.Concatenate(axis=-1)([n2_Backbone_n13_mixed_0_n1_Conv2D_BN_n2_Activation, n2_Backbone_n13_mixed_0_n3_Conv2D_BN_n2_Activation, n2_Backbone_n13_mixed_0_n6_Conv2D_BN_n2_Activation, n2_Backbone_n13_mixed_0_n8_Conv2D_BN_n2_Activation])
        else:
            n2_Backbone_n13_mixed_0_n10_Concatenate = layer_60a5c90c82ffc54caedc45b5.Concatenate(axis=-1)(*[n2_Backbone_n13_mixed_0_n1_Conv2D_BN_n2_Activation, n2_Backbone_n13_mixed_0_n3_Conv2D_BN_n2_Activation, n2_Backbone_n13_mixed_0_n6_Conv2D_BN_n2_Activation, n2_Backbone_n13_mixed_0_n8_Conv2D_BN_n2_Activation])
        n2_Backbone_n14_mixed_3_n2_Activation = layer_60a5c90c82ffc54caedc45c1.Activation(activation='linear')(n2_Backbone_n13_mixed_0_n10_Concatenate)
        n2_Backbone_n14_mixed_3_n3_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc45c5.Conv2D(filters=64, kernel_size=[1, 1], strides=[1, 1], padding='valid', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n14_mixed_3_n2_Activation)
        n2_Backbone_n14_mixed_3_n3_Conv2D_BN_n2_BatchNormalization = layer_60a5c90c82ffc54caedc45c7.BatchNormalization()(n2_Backbone_n14_mixed_3_n3_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n14_mixed_3_n3_Conv2D_BN_n3_Activation = layer_60a5c90c82ffc54caedc45c9.Activation(activation='relu')(n2_Backbone_n14_mixed_3_n3_Conv2D_BN_n2_BatchNormalization)
        n2_Backbone_n14_mixed_3_n4_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc45cd.Conv2D(filters=96, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n14_mixed_3_n3_Conv2D_BN_n3_Activation)
        n2_Backbone_n14_mixed_3_n4_Conv2D_BN_n2_BatchNormalization = layer_60a5c90c82ffc54caedc45cf.BatchNormalization()(n2_Backbone_n14_mixed_3_n4_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n14_mixed_3_n4_Conv2D_BN_n3_Activation = layer_60a5c90c82ffc54caedc45d1.Activation(activation='relu')(n2_Backbone_n14_mixed_3_n4_Conv2D_BN_n2_BatchNormalization)
        n2_Backbone_n14_mixed_3_n5_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc45d5.Conv2D(filters=96, kernel_size=[3, 3], strides=[2, 2], padding='valid', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n14_mixed_3_n4_Conv2D_BN_n3_Activation)
        n2_Backbone_n14_mixed_3_n5_Conv2D_BN_n2_BatchNormalization = layer_60a5c90c82ffc54caedc45d7.BatchNormalization()(n2_Backbone_n14_mixed_3_n5_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n14_mixed_3_n5_Conv2D_BN_n3_Activation = layer_60a5c90c82ffc54caedc45d9.Activation(activation='relu')(n2_Backbone_n14_mixed_3_n5_Conv2D_BN_n2_BatchNormalization)
        n2_Backbone_n14_mixed_3_n6_MaxPooling2D = layer_60a5c90c82ffc54caedc45db.MaxPooling2D(pool_size=[3, 3], strides=[2, 2], padding='valid')(n2_Backbone_n14_mixed_3_n2_Activation)
        n2_Backbone_n14_mixed_3_n1_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc45bb.Conv2D(filters=384, kernel_size=[3, 3], strides=[2, 2], padding='valid', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n14_mixed_3_n2_Activation)
        n2_Backbone_n14_mixed_3_n1_Conv2D_BN_n2_BatchNormalization = layer_60a5c90c82ffc54caedc45bd.BatchNormalization()(n2_Backbone_n14_mixed_3_n1_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n14_mixed_3_n1_Conv2D_BN_n3_Activation = layer_60a5c90c82ffc54caedc45bf.Activation(activation='relu')(n2_Backbone_n14_mixed_3_n1_Conv2D_BN_n2_BatchNormalization)
        num_args = len(inspect.getfullargspec(layer_60a5c90c82ffc54caedc45df.Concatenate(axis=-1).call).args)
        if num_args == 2:
            n2_Backbone_n14_mixed_3_n7_Concatenate = layer_60a5c90c82ffc54caedc45df.Concatenate(axis=-1)([n2_Backbone_n14_mixed_3_n6_MaxPooling2D, n2_Backbone_n14_mixed_3_n1_Conv2D_BN_n3_Activation, n2_Backbone_n14_mixed_3_n5_Conv2D_BN_n3_Activation])
        else:
            n2_Backbone_n14_mixed_3_n7_Concatenate = layer_60a5c90c82ffc54caedc45df.Concatenate(axis=-1)(*[n2_Backbone_n14_mixed_3_n6_MaxPooling2D, n2_Backbone_n14_mixed_3_n1_Conv2D_BN_n3_Activation, n2_Backbone_n14_mixed_3_n5_Conv2D_BN_n3_Activation])
        n2_Backbone_n15_mixed_0_n7_Activation = layer_60a5c90c82ffc54caedc4613.Activation(activation='linear')(n2_Backbone_n14_mixed_3_n7_Concatenate)
        n2_Backbone_n15_mixed_0_n1_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc45e5.Conv2D(filters=192, kernel_size=[1, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n15_mixed_0_n7_Activation)
        n2_Backbone_n15_mixed_0_n1_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc45e9.BatchNormalization()(n2_Backbone_n15_mixed_0_n1_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n15_mixed_0_n2_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc45ed.Conv2D(filters=128, kernel_size=[1, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n15_mixed_0_n7_Activation)
        n2_Backbone_n15_mixed_0_n2_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc45f1.BatchNormalization()(n2_Backbone_n15_mixed_0_n2_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n15_mixed_0_n4_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc4603.Conv2D(filters=128, kernel_size=[1, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n15_mixed_0_n7_Activation)
        n2_Backbone_n15_mixed_0_n4_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc4607.BatchNormalization()(n2_Backbone_n15_mixed_0_n4_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n15_mixed_0_n5_AveragePooling2D = layer_60a5c90c82ffc54caedc4609.AveragePooling2D(pool_size=[3, 3], strides=[1, 1], padding='same')(n2_Backbone_n15_mixed_0_n7_Activation)
        n2_Backbone_n15_mixed_0_n6_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc460d.Conv2D(filters=192, kernel_size=[1, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n15_mixed_0_n5_AveragePooling2D)
        n2_Backbone_n15_mixed_0_n6_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc4611.BatchNormalization()(n2_Backbone_n15_mixed_0_n6_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n15_mixed_0_n1_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc45e7.Activation(activation='relu')(n2_Backbone_n15_mixed_0_n1_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n15_mixed_0_n2_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc45ef.Activation(activation='relu')(n2_Backbone_n15_mixed_0_n2_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n15_mixed_0_n3_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc45f5.Conv2D(filters=128, kernel_size=[1, 7], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n15_mixed_0_n2_Conv2D_BN_n2_Activation)
        n2_Backbone_n15_mixed_0_n3_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc45f9.BatchNormalization()(n2_Backbone_n15_mixed_0_n3_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n15_mixed_0_n4_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc4605.Activation(activation='relu')(n2_Backbone_n15_mixed_0_n4_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n15_mixed_0_n6_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc460f.Activation(activation='relu')(n2_Backbone_n15_mixed_0_n6_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n15_mixed_0_n9_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc461c.Conv2D(filters=128, kernel_size=[1, 7], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n15_mixed_0_n4_Conv2D_BN_n2_Activation)
        n2_Backbone_n15_mixed_0_n9_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc4620.BatchNormalization()(n2_Backbone_n15_mixed_0_n9_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n15_mixed_0_n3_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc45f7.Activation(activation='relu')(n2_Backbone_n15_mixed_0_n3_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n15_mixed_0_n3_Conv2D_BN_n4_Conv2D = layer_60a5c90c82ffc54caedc45fb.Conv2D(filters=192, kernel_size=[7, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n15_mixed_0_n3_Conv2D_BN_n2_Activation)
        n2_Backbone_n15_mixed_0_n3_Conv2D_BN_n5_BatchNormalization = layer_60a5c90c82ffc54caedc45fd.BatchNormalization()(n2_Backbone_n15_mixed_0_n3_Conv2D_BN_n4_Conv2D)
        n2_Backbone_n15_mixed_0_n3_Conv2D_BN_n6_Activation = layer_60a5c90c82ffc54caedc45ff.Activation(activation='relu')(n2_Backbone_n15_mixed_0_n3_Conv2D_BN_n5_BatchNormalization)
        n2_Backbone_n15_mixed_0_n9_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc461e.Activation(activation='relu')(n2_Backbone_n15_mixed_0_n9_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n15_mixed_0_n9_Conv2D_BN_n4_Conv2D = layer_60a5c90c82ffc54caedc4622.Conv2D(filters=128, kernel_size=[7, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n15_mixed_0_n9_Conv2D_BN_n2_Activation)
        n2_Backbone_n15_mixed_0_n9_Conv2D_BN_n5_BatchNormalization = layer_60a5c90c82ffc54caedc4624.BatchNormalization()(n2_Backbone_n15_mixed_0_n9_Conv2D_BN_n4_Conv2D)
        n2_Backbone_n15_mixed_0_n9_Conv2D_BN_n6_Activation = layer_60a5c90c82ffc54caedc4626.Activation(activation='relu')(n2_Backbone_n15_mixed_0_n9_Conv2D_BN_n5_BatchNormalization)
        n2_Backbone_n15_mixed_0_n10_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc462a.Conv2D(filters=128, kernel_size=[1, 7], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n15_mixed_0_n9_Conv2D_BN_n6_Activation)
        n2_Backbone_n15_mixed_0_n10_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc462e.BatchNormalization()(n2_Backbone_n15_mixed_0_n10_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n15_mixed_0_n10_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc462c.Activation(activation='relu')(n2_Backbone_n15_mixed_0_n10_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n15_mixed_0_n10_Conv2D_BN_n4_Conv2D = layer_60a5c90c82ffc54caedc4630.Conv2D(filters=192, kernel_size=[7, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n15_mixed_0_n10_Conv2D_BN_n2_Activation)
        n2_Backbone_n15_mixed_0_n10_Conv2D_BN_n5_BatchNormalization = layer_60a5c90c82ffc54caedc4632.BatchNormalization()(n2_Backbone_n15_mixed_0_n10_Conv2D_BN_n4_Conv2D)
        n2_Backbone_n15_mixed_0_n10_Conv2D_BN_n6_Activation = layer_60a5c90c82ffc54caedc4634.Activation(activation='relu')(n2_Backbone_n15_mixed_0_n10_Conv2D_BN_n5_BatchNormalization)
        num_args = len(inspect.getfullargspec(layer_60a5c90c82ffc54caedc4618.Concatenate(axis=-1).call).args)
        if num_args == 2:
            n2_Backbone_n15_mixed_0_n8_Concatenate = layer_60a5c90c82ffc54caedc4618.Concatenate(axis=-1)([n2_Backbone_n15_mixed_0_n1_Conv2D_BN_n2_Activation, n2_Backbone_n15_mixed_0_n6_Conv2D_BN_n2_Activation, n2_Backbone_n15_mixed_0_n3_Conv2D_BN_n6_Activation, n2_Backbone_n15_mixed_0_n10_Conv2D_BN_n6_Activation])
        else:
            n2_Backbone_n15_mixed_0_n8_Concatenate = layer_60a5c90c82ffc54caedc4618.Concatenate(axis=-1)(*[n2_Backbone_n15_mixed_0_n1_Conv2D_BN_n2_Activation, n2_Backbone_n15_mixed_0_n6_Conv2D_BN_n2_Activation, n2_Backbone_n15_mixed_0_n3_Conv2D_BN_n6_Activation, n2_Backbone_n15_mixed_0_n10_Conv2D_BN_n6_Activation])
        n2_Backbone_n16_mixed_0_n7_Activation = layer_60a5c90c82ffc54caedc4668.Activation(activation='linear')(n2_Backbone_n15_mixed_0_n8_Concatenate)
        n2_Backbone_n16_mixed_0_n1_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc463a.Conv2D(filters=192, kernel_size=[1, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n16_mixed_0_n7_Activation)
        n2_Backbone_n16_mixed_0_n1_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc463e.BatchNormalization()(n2_Backbone_n16_mixed_0_n1_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n16_mixed_0_n2_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc4642.Conv2D(filters=160, kernel_size=[1, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n16_mixed_0_n7_Activation)
        n2_Backbone_n16_mixed_0_n2_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc4646.BatchNormalization()(n2_Backbone_n16_mixed_0_n2_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n16_mixed_0_n4_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc4658.Conv2D(filters=160, kernel_size=[1, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n16_mixed_0_n7_Activation)
        n2_Backbone_n16_mixed_0_n4_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc465c.BatchNormalization()(n2_Backbone_n16_mixed_0_n4_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n16_mixed_0_n5_AveragePooling2D = layer_60a5c90c82ffc54caedc465e.AveragePooling2D(pool_size=[3, 3], strides=[1, 1], padding='same')(n2_Backbone_n16_mixed_0_n7_Activation)
        n2_Backbone_n16_mixed_0_n6_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc4662.Conv2D(filters=192, kernel_size=[1, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n16_mixed_0_n5_AveragePooling2D)
        n2_Backbone_n16_mixed_0_n6_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc4666.BatchNormalization()(n2_Backbone_n16_mixed_0_n6_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n16_mixed_0_n1_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc463c.Activation(activation='relu')(n2_Backbone_n16_mixed_0_n1_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n16_mixed_0_n2_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc4644.Activation(activation='relu')(n2_Backbone_n16_mixed_0_n2_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n16_mixed_0_n3_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc464a.Conv2D(filters=160, kernel_size=[1, 7], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n16_mixed_0_n2_Conv2D_BN_n2_Activation)
        n2_Backbone_n16_mixed_0_n3_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc464e.BatchNormalization()(n2_Backbone_n16_mixed_0_n3_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n16_mixed_0_n4_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc465a.Activation(activation='relu')(n2_Backbone_n16_mixed_0_n4_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n16_mixed_0_n6_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc4664.Activation(activation='relu')(n2_Backbone_n16_mixed_0_n6_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n16_mixed_0_n9_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc4671.Conv2D(filters=160, kernel_size=[1, 7], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n16_mixed_0_n4_Conv2D_BN_n2_Activation)
        n2_Backbone_n16_mixed_0_n9_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc4675.BatchNormalization()(n2_Backbone_n16_mixed_0_n9_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n16_mixed_0_n3_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc464c.Activation(activation='relu')(n2_Backbone_n16_mixed_0_n3_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n16_mixed_0_n3_Conv2D_BN_n4_Conv2D = layer_60a5c90c82ffc54caedc4650.Conv2D(filters=192, kernel_size=[7, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n16_mixed_0_n3_Conv2D_BN_n2_Activation)
        n2_Backbone_n16_mixed_0_n3_Conv2D_BN_n5_BatchNormalization = layer_60a5c90c82ffc54caedc4652.BatchNormalization()(n2_Backbone_n16_mixed_0_n3_Conv2D_BN_n4_Conv2D)
        n2_Backbone_n16_mixed_0_n3_Conv2D_BN_n6_Activation = layer_60a5c90c82ffc54caedc4654.Activation(activation='relu')(n2_Backbone_n16_mixed_0_n3_Conv2D_BN_n5_BatchNormalization)
        n2_Backbone_n16_mixed_0_n9_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc4673.Activation(activation='relu')(n2_Backbone_n16_mixed_0_n9_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n16_mixed_0_n9_Conv2D_BN_n4_Conv2D = layer_60a5c90c82ffc54caedc4677.Conv2D(filters=160, kernel_size=[7, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n16_mixed_0_n9_Conv2D_BN_n2_Activation)
        n2_Backbone_n16_mixed_0_n9_Conv2D_BN_n5_BatchNormalization = layer_60a5c90c82ffc54caedc4679.BatchNormalization()(n2_Backbone_n16_mixed_0_n9_Conv2D_BN_n4_Conv2D)
        n2_Backbone_n16_mixed_0_n9_Conv2D_BN_n6_Activation = layer_60a5c90c82ffc54caedc467b.Activation(activation='relu')(n2_Backbone_n16_mixed_0_n9_Conv2D_BN_n5_BatchNormalization)
        n2_Backbone_n16_mixed_0_n10_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc467f.Conv2D(filters=160, kernel_size=[1, 7], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n16_mixed_0_n9_Conv2D_BN_n6_Activation)
        n2_Backbone_n16_mixed_0_n10_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc4683.BatchNormalization()(n2_Backbone_n16_mixed_0_n10_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n16_mixed_0_n10_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc4681.Activation(activation='relu')(n2_Backbone_n16_mixed_0_n10_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n16_mixed_0_n10_Conv2D_BN_n4_Conv2D = layer_60a5c90c82ffc54caedc4685.Conv2D(filters=192, kernel_size=[7, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n16_mixed_0_n10_Conv2D_BN_n2_Activation)
        n2_Backbone_n16_mixed_0_n10_Conv2D_BN_n5_BatchNormalization = layer_60a5c90c82ffc54caedc4687.BatchNormalization()(n2_Backbone_n16_mixed_0_n10_Conv2D_BN_n4_Conv2D)
        n2_Backbone_n16_mixed_0_n10_Conv2D_BN_n6_Activation = layer_60a5c90c82ffc54caedc4689.Activation(activation='relu')(n2_Backbone_n16_mixed_0_n10_Conv2D_BN_n5_BatchNormalization)
        num_args = len(inspect.getfullargspec(layer_60a5c90c82ffc54caedc466d.Concatenate(axis=-1).call).args)
        if num_args == 2:
            n2_Backbone_n16_mixed_0_n8_Concatenate = layer_60a5c90c82ffc54caedc466d.Concatenate(axis=-1)([n2_Backbone_n16_mixed_0_n1_Conv2D_BN_n2_Activation, n2_Backbone_n16_mixed_0_n6_Conv2D_BN_n2_Activation, n2_Backbone_n16_mixed_0_n3_Conv2D_BN_n6_Activation, n2_Backbone_n16_mixed_0_n10_Conv2D_BN_n6_Activation])
        else:
            n2_Backbone_n16_mixed_0_n8_Concatenate = layer_60a5c90c82ffc54caedc466d.Concatenate(axis=-1)(*[n2_Backbone_n16_mixed_0_n1_Conv2D_BN_n2_Activation, n2_Backbone_n16_mixed_0_n6_Conv2D_BN_n2_Activation, n2_Backbone_n16_mixed_0_n3_Conv2D_BN_n6_Activation, n2_Backbone_n16_mixed_0_n10_Conv2D_BN_n6_Activation])
        n2_Backbone_n18_mixed_0_n7_Activation = layer_60a5c90c82ffc54caedc4712.Activation(activation='linear')(n2_Backbone_n16_mixed_0_n8_Concatenate)
        n2_Backbone_n18_mixed_0_n1_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc46e4.Conv2D(filters=192, kernel_size=[1, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n18_mixed_0_n7_Activation)
        n2_Backbone_n18_mixed_0_n1_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc46e8.BatchNormalization()(n2_Backbone_n18_mixed_0_n1_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n18_mixed_0_n2_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc46ec.Conv2D(filters=160, kernel_size=[1, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n18_mixed_0_n7_Activation)
        n2_Backbone_n18_mixed_0_n2_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc46f0.BatchNormalization()(n2_Backbone_n18_mixed_0_n2_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n18_mixed_0_n4_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc4702.Conv2D(filters=160, kernel_size=[1, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n18_mixed_0_n7_Activation)
        n2_Backbone_n18_mixed_0_n4_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc4706.BatchNormalization()(n2_Backbone_n18_mixed_0_n4_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n18_mixed_0_n5_AveragePooling2D = layer_60a5c90c82ffc54caedc4708.AveragePooling2D(pool_size=[3, 3], strides=[1, 1], padding='same')(n2_Backbone_n18_mixed_0_n7_Activation)
        n2_Backbone_n18_mixed_0_n6_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc470c.Conv2D(filters=192, kernel_size=[1, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n18_mixed_0_n5_AveragePooling2D)
        n2_Backbone_n18_mixed_0_n6_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc4710.BatchNormalization()(n2_Backbone_n18_mixed_0_n6_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n18_mixed_0_n1_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc46e6.Activation(activation='relu')(n2_Backbone_n18_mixed_0_n1_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n18_mixed_0_n2_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc46ee.Activation(activation='relu')(n2_Backbone_n18_mixed_0_n2_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n18_mixed_0_n3_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc46f4.Conv2D(filters=160, kernel_size=[1, 7], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n18_mixed_0_n2_Conv2D_BN_n2_Activation)
        n2_Backbone_n18_mixed_0_n3_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc46f8.BatchNormalization()(n2_Backbone_n18_mixed_0_n3_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n18_mixed_0_n4_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc4704.Activation(activation='relu')(n2_Backbone_n18_mixed_0_n4_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n18_mixed_0_n6_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc470e.Activation(activation='relu')(n2_Backbone_n18_mixed_0_n6_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n18_mixed_0_n9_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc471b.Conv2D(filters=160, kernel_size=[1, 7], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n18_mixed_0_n4_Conv2D_BN_n2_Activation)
        n2_Backbone_n18_mixed_0_n9_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc471f.BatchNormalization()(n2_Backbone_n18_mixed_0_n9_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n18_mixed_0_n3_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc46f6.Activation(activation='relu')(n2_Backbone_n18_mixed_0_n3_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n18_mixed_0_n3_Conv2D_BN_n4_Conv2D = layer_60a5c90c82ffc54caedc46fa.Conv2D(filters=192, kernel_size=[7, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n18_mixed_0_n3_Conv2D_BN_n2_Activation)
        n2_Backbone_n18_mixed_0_n3_Conv2D_BN_n5_BatchNormalization = layer_60a5c90c82ffc54caedc46fc.BatchNormalization()(n2_Backbone_n18_mixed_0_n3_Conv2D_BN_n4_Conv2D)
        n2_Backbone_n18_mixed_0_n3_Conv2D_BN_n6_Activation = layer_60a5c90c82ffc54caedc46fe.Activation(activation='relu')(n2_Backbone_n18_mixed_0_n3_Conv2D_BN_n5_BatchNormalization)
        n2_Backbone_n18_mixed_0_n9_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc471d.Activation(activation='relu')(n2_Backbone_n18_mixed_0_n9_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n18_mixed_0_n9_Conv2D_BN_n4_Conv2D = layer_60a5c90c82ffc54caedc4721.Conv2D(filters=160, kernel_size=[7, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n18_mixed_0_n9_Conv2D_BN_n2_Activation)
        n2_Backbone_n18_mixed_0_n9_Conv2D_BN_n5_BatchNormalization = layer_60a5c90c82ffc54caedc4723.BatchNormalization()(n2_Backbone_n18_mixed_0_n9_Conv2D_BN_n4_Conv2D)
        n2_Backbone_n18_mixed_0_n9_Conv2D_BN_n6_Activation = layer_60a5c90c82ffc54caedc4725.Activation(activation='relu')(n2_Backbone_n18_mixed_0_n9_Conv2D_BN_n5_BatchNormalization)
        n2_Backbone_n18_mixed_0_n10_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc4729.Conv2D(filters=160, kernel_size=[1, 7], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n18_mixed_0_n9_Conv2D_BN_n6_Activation)
        n2_Backbone_n18_mixed_0_n10_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc472d.BatchNormalization()(n2_Backbone_n18_mixed_0_n10_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n18_mixed_0_n10_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc472b.Activation(activation='relu')(n2_Backbone_n18_mixed_0_n10_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n18_mixed_0_n10_Conv2D_BN_n4_Conv2D = layer_60a5c90c82ffc54caedc472f.Conv2D(filters=192, kernel_size=[7, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n18_mixed_0_n10_Conv2D_BN_n2_Activation)
        n2_Backbone_n18_mixed_0_n10_Conv2D_BN_n5_BatchNormalization = layer_60a5c90c82ffc54caedc4731.BatchNormalization()(n2_Backbone_n18_mixed_0_n10_Conv2D_BN_n4_Conv2D)
        n2_Backbone_n18_mixed_0_n10_Conv2D_BN_n6_Activation = layer_60a5c90c82ffc54caedc4733.Activation(activation='relu')(n2_Backbone_n18_mixed_0_n10_Conv2D_BN_n5_BatchNormalization)
        num_args = len(inspect.getfullargspec(layer_60a5c90c82ffc54caedc4717.Concatenate(axis=-1).call).args)
        if num_args == 2:
            n2_Backbone_n18_mixed_0_n8_Concatenate = layer_60a5c90c82ffc54caedc4717.Concatenate(axis=-1)([n2_Backbone_n18_mixed_0_n1_Conv2D_BN_n2_Activation, n2_Backbone_n18_mixed_0_n6_Conv2D_BN_n2_Activation, n2_Backbone_n18_mixed_0_n3_Conv2D_BN_n6_Activation, n2_Backbone_n18_mixed_0_n10_Conv2D_BN_n6_Activation])
        else:
            n2_Backbone_n18_mixed_0_n8_Concatenate = layer_60a5c90c82ffc54caedc4717.Concatenate(axis=-1)(*[n2_Backbone_n18_mixed_0_n1_Conv2D_BN_n2_Activation, n2_Backbone_n18_mixed_0_n6_Conv2D_BN_n2_Activation, n2_Backbone_n18_mixed_0_n3_Conv2D_BN_n6_Activation, n2_Backbone_n18_mixed_0_n10_Conv2D_BN_n6_Activation])
        n2_Backbone_n17_mixed_0_n7_Activation = layer_60a5c90c82ffc54caedc46bd.Activation(activation='linear')(n2_Backbone_n18_mixed_0_n8_Concatenate)
        n2_Backbone_n17_mixed_0_n1_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc468f.Conv2D(filters=192, kernel_size=[1, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n17_mixed_0_n7_Activation)
        n2_Backbone_n17_mixed_0_n1_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc4693.BatchNormalization()(n2_Backbone_n17_mixed_0_n1_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n17_mixed_0_n2_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc4697.Conv2D(filters=192, kernel_size=[1, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n17_mixed_0_n7_Activation)
        n2_Backbone_n17_mixed_0_n2_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc469b.BatchNormalization()(n2_Backbone_n17_mixed_0_n2_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n17_mixed_0_n4_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc46ad.Conv2D(filters=192, kernel_size=[1, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n17_mixed_0_n7_Activation)
        n2_Backbone_n17_mixed_0_n4_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc46b1.BatchNormalization()(n2_Backbone_n17_mixed_0_n4_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n17_mixed_0_n5_AveragePooling2D = layer_60a5c90c82ffc54caedc46b3.AveragePooling2D(pool_size=[3, 3], strides=[1, 1], padding='same')(n2_Backbone_n17_mixed_0_n7_Activation)
        n2_Backbone_n17_mixed_0_n6_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc46b7.Conv2D(filters=192, kernel_size=[1, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n17_mixed_0_n5_AveragePooling2D)
        n2_Backbone_n17_mixed_0_n6_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc46bb.BatchNormalization()(n2_Backbone_n17_mixed_0_n6_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n17_mixed_0_n1_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc4691.Activation(activation='relu')(n2_Backbone_n17_mixed_0_n1_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n17_mixed_0_n2_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc4699.Activation(activation='relu')(n2_Backbone_n17_mixed_0_n2_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n17_mixed_0_n3_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc469f.Conv2D(filters=192, kernel_size=[1, 7], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n17_mixed_0_n2_Conv2D_BN_n2_Activation)
        n2_Backbone_n17_mixed_0_n3_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc46a3.BatchNormalization()(n2_Backbone_n17_mixed_0_n3_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n17_mixed_0_n4_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc46af.Activation(activation='relu')(n2_Backbone_n17_mixed_0_n4_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n17_mixed_0_n6_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc46b9.Activation(activation='relu')(n2_Backbone_n17_mixed_0_n6_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n17_mixed_0_n9_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc46c6.Conv2D(filters=192, kernel_size=[1, 7], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n17_mixed_0_n4_Conv2D_BN_n2_Activation)
        n2_Backbone_n17_mixed_0_n9_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc46ca.BatchNormalization()(n2_Backbone_n17_mixed_0_n9_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n17_mixed_0_n3_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc46a1.Activation(activation='relu')(n2_Backbone_n17_mixed_0_n3_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n17_mixed_0_n3_Conv2D_BN_n4_Conv2D = layer_60a5c90c82ffc54caedc46a5.Conv2D(filters=192, kernel_size=[7, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n17_mixed_0_n3_Conv2D_BN_n2_Activation)
        n2_Backbone_n17_mixed_0_n3_Conv2D_BN_n5_BatchNormalization = layer_60a5c90c82ffc54caedc46a7.BatchNormalization()(n2_Backbone_n17_mixed_0_n3_Conv2D_BN_n4_Conv2D)
        n2_Backbone_n17_mixed_0_n3_Conv2D_BN_n6_Activation = layer_60a5c90c82ffc54caedc46a9.Activation(activation='relu')(n2_Backbone_n17_mixed_0_n3_Conv2D_BN_n5_BatchNormalization)
        n2_Backbone_n17_mixed_0_n9_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc46c8.Activation(activation='relu')(n2_Backbone_n17_mixed_0_n9_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n17_mixed_0_n9_Conv2D_BN_n4_Conv2D = layer_60a5c90c82ffc54caedc46cc.Conv2D(filters=160, kernel_size=[7, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n17_mixed_0_n9_Conv2D_BN_n2_Activation)
        n2_Backbone_n17_mixed_0_n9_Conv2D_BN_n5_BatchNormalization = layer_60a5c90c82ffc54caedc46ce.BatchNormalization()(n2_Backbone_n17_mixed_0_n9_Conv2D_BN_n4_Conv2D)
        n2_Backbone_n17_mixed_0_n9_Conv2D_BN_n6_Activation = layer_60a5c90c82ffc54caedc46d0.Activation(activation='relu')(n2_Backbone_n17_mixed_0_n9_Conv2D_BN_n5_BatchNormalization)
        n2_Backbone_n17_mixed_0_n10_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc46d4.Conv2D(filters=192, kernel_size=[1, 7], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n17_mixed_0_n9_Conv2D_BN_n6_Activation)
        n2_Backbone_n17_mixed_0_n10_Conv2D_BN_n3_BatchNormalization = layer_60a5c90c82ffc54caedc46d8.BatchNormalization()(n2_Backbone_n17_mixed_0_n10_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n17_mixed_0_n10_Conv2D_BN_n2_Activation = layer_60a5c90c82ffc54caedc46d6.Activation(activation='relu')(n2_Backbone_n17_mixed_0_n10_Conv2D_BN_n3_BatchNormalization)
        n2_Backbone_n17_mixed_0_n10_Conv2D_BN_n4_Conv2D = layer_60a5c90c82ffc54caedc46da.Conv2D(filters=192, kernel_size=[7, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n17_mixed_0_n10_Conv2D_BN_n2_Activation)
        n2_Backbone_n17_mixed_0_n10_Conv2D_BN_n5_BatchNormalization = layer_60a5c90c82ffc54caedc46dc.BatchNormalization()(n2_Backbone_n17_mixed_0_n10_Conv2D_BN_n4_Conv2D)
        n2_Backbone_n17_mixed_0_n10_Conv2D_BN_n6_Activation = layer_60a5c90c82ffc54caedc46de.Activation(activation='relu')(n2_Backbone_n17_mixed_0_n10_Conv2D_BN_n5_BatchNormalization)
        num_args = len(inspect.getfullargspec(layer_60a5c90c82ffc54caedc46c2.Concatenate(axis=-1).call).args)
        if num_args == 2:
            n2_Backbone_n17_mixed_0_n8_Concatenate = layer_60a5c90c82ffc54caedc46c2.Concatenate(axis=-1)([n2_Backbone_n17_mixed_0_n1_Conv2D_BN_n2_Activation, n2_Backbone_n17_mixed_0_n6_Conv2D_BN_n2_Activation, n2_Backbone_n17_mixed_0_n3_Conv2D_BN_n6_Activation, n2_Backbone_n17_mixed_0_n10_Conv2D_BN_n6_Activation])
        else:
            n2_Backbone_n17_mixed_0_n8_Concatenate = layer_60a5c90c82ffc54caedc46c2.Concatenate(axis=-1)(*[n2_Backbone_n17_mixed_0_n1_Conv2D_BN_n2_Activation, n2_Backbone_n17_mixed_0_n6_Conv2D_BN_n2_Activation, n2_Backbone_n17_mixed_0_n3_Conv2D_BN_n6_Activation, n2_Backbone_n17_mixed_0_n10_Conv2D_BN_n6_Activation])
        n2_Backbone_n19_mixed_3_n2_Activation = layer_60a5c90c82ffc54caedc473f.Activation(activation='linear')(n2_Backbone_n17_mixed_0_n8_Concatenate)
        n2_Backbone_n19_mixed_3_n3_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc4743.Conv2D(filters=192, kernel_size=[1, 1], strides=[1, 1], padding='valid', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n19_mixed_3_n2_Activation)
        n2_Backbone_n19_mixed_3_n3_Conv2D_BN_n2_BatchNormalization = layer_60a5c90c82ffc54caedc4745.BatchNormalization()(n2_Backbone_n19_mixed_3_n3_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n19_mixed_3_n3_Conv2D_BN_n3_Activation = layer_60a5c90c82ffc54caedc4747.Activation(activation='relu')(n2_Backbone_n19_mixed_3_n3_Conv2D_BN_n2_BatchNormalization)
        n2_Backbone_n19_mixed_3_n4_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc474b.Conv2D(filters=192, kernel_size=[1, 7], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n19_mixed_3_n3_Conv2D_BN_n3_Activation)
        n2_Backbone_n19_mixed_3_n4_Conv2D_BN_n2_BatchNormalization = layer_60a5c90c82ffc54caedc474d.BatchNormalization()(n2_Backbone_n19_mixed_3_n4_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n19_mixed_3_n4_Conv2D_BN_n3_Activation = layer_60a5c90c82ffc54caedc474f.Activation(activation='relu')(n2_Backbone_n19_mixed_3_n4_Conv2D_BN_n2_BatchNormalization)
        n2_Backbone_n19_mixed_3_n4_Conv2D_BN_n4_Conv2D = layer_60a5c90c82ffc54caedc4751.Conv2D(filters=192, kernel_size=[7, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n19_mixed_3_n4_Conv2D_BN_n3_Activation)
        n2_Backbone_n19_mixed_3_n4_Conv2D_BN_n5_BatchNormalization = layer_60a5c90c82ffc54caedc4753.BatchNormalization()(n2_Backbone_n19_mixed_3_n4_Conv2D_BN_n4_Conv2D)
        n2_Backbone_n19_mixed_3_n4_Conv2D_BN_n6_Activation = layer_60a5c90c82ffc54caedc4755.Activation(activation='relu')(n2_Backbone_n19_mixed_3_n4_Conv2D_BN_n5_BatchNormalization)
        n2_Backbone_n19_mixed_3_n5_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc4759.Conv2D(filters=192, kernel_size=[3, 3], strides=[2, 2], padding='valid', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n19_mixed_3_n4_Conv2D_BN_n6_Activation)
        n2_Backbone_n19_mixed_3_n5_Conv2D_BN_n2_BatchNormalization = layer_60a5c90c82ffc54caedc475b.BatchNormalization()(n2_Backbone_n19_mixed_3_n5_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n19_mixed_3_n5_Conv2D_BN_n3_Activation = layer_60a5c90c82ffc54caedc475d.Activation(activation='relu')(n2_Backbone_n19_mixed_3_n5_Conv2D_BN_n2_BatchNormalization)
        n2_Backbone_n19_mixed_3_n6_MaxPooling2D = layer_60a5c90c82ffc54caedc475f.MaxPooling2D(pool_size=[3, 3], strides=[2, 2], padding='valid')(n2_Backbone_n19_mixed_3_n2_Activation)
        n2_Backbone_n19_mixed_3_n1_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc4739.Conv2D(filters=192, kernel_size=[1, 1], strides=[1, 1], padding='valid', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n19_mixed_3_n2_Activation)
        n2_Backbone_n19_mixed_3_n1_Conv2D_BN_n2_BatchNormalization = layer_60a5c90c82ffc54caedc473b.BatchNormalization()(n2_Backbone_n19_mixed_3_n1_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n19_mixed_3_n1_Conv2D_BN_n3_Activation = layer_60a5c90c82ffc54caedc473d.Activation(activation='relu')(n2_Backbone_n19_mixed_3_n1_Conv2D_BN_n2_BatchNormalization)
        n2_Backbone_n19_mixed_3_n8_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc4767.Conv2D(filters=320, kernel_size=[3, 3], strides=[2, 2], padding='valid', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n19_mixed_3_n1_Conv2D_BN_n3_Activation)
        n2_Backbone_n19_mixed_3_n8_Conv2D_BN_n2_BatchNormalization = layer_60a5c90c82ffc54caedc4769.BatchNormalization()(n2_Backbone_n19_mixed_3_n8_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n19_mixed_3_n8_Conv2D_BN_n3_Activation = layer_60a5c90c82ffc54caedc476b.Activation(activation='relu')(n2_Backbone_n19_mixed_3_n8_Conv2D_BN_n2_BatchNormalization)
        num_args = len(inspect.getfullargspec(layer_60a5c90c82ffc54caedc4763.Concatenate(axis=-1).call).args)
        if num_args == 2:
            n2_Backbone_n19_mixed_3_n7_Concatenate = layer_60a5c90c82ffc54caedc4763.Concatenate(axis=-1)([n2_Backbone_n19_mixed_3_n6_MaxPooling2D, n2_Backbone_n19_mixed_3_n5_Conv2D_BN_n3_Activation, n2_Backbone_n19_mixed_3_n8_Conv2D_BN_n3_Activation])
        else:
            n2_Backbone_n19_mixed_3_n7_Concatenate = layer_60a5c90c82ffc54caedc4763.Concatenate(axis=-1)(*[n2_Backbone_n19_mixed_3_n6_MaxPooling2D, n2_Backbone_n19_mixed_3_n5_Conv2D_BN_n3_Activation, n2_Backbone_n19_mixed_3_n8_Conv2D_BN_n3_Activation])
        n2_Backbone_n20_mixed_9_n2_Activation = layer_60a5c90c82ffc54caedc4777.Activation(activation='linear')(n2_Backbone_n19_mixed_3_n7_Concatenate)
        n2_Backbone_n20_mixed_9_n3_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc477b.Conv2D(filters=384, kernel_size=[1, 1], strides=[1, 1], padding='valid', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n20_mixed_9_n2_Activation)
        n2_Backbone_n20_mixed_9_n3_Conv2D_BN_n2_BatchNormalization = layer_60a5c90c82ffc54caedc477d.BatchNormalization()(n2_Backbone_n20_mixed_9_n3_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n20_mixed_9_n3_Conv2D_BN_n3_Activation = layer_60a5c90c82ffc54caedc477f.Activation(activation='relu')(n2_Backbone_n20_mixed_9_n3_Conv2D_BN_n2_BatchNormalization)
        n2_Backbone_n20_mixed_9_n4_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc4783.Conv2D(filters=384, kernel_size=[1, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n20_mixed_9_n3_Conv2D_BN_n3_Activation)
        n2_Backbone_n20_mixed_9_n4_Conv2D_BN_n2_BatchNormalization = layer_60a5c90c82ffc54caedc4785.BatchNormalization()(n2_Backbone_n20_mixed_9_n4_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n20_mixed_9_n4_Conv2D_BN_n3_Activation = layer_60a5c90c82ffc54caedc4787.Activation(activation='relu')(n2_Backbone_n20_mixed_9_n4_Conv2D_BN_n2_BatchNormalization)
        n2_Backbone_n20_mixed_9_n5_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc478b.Conv2D(filters=384, kernel_size=[3, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n20_mixed_9_n3_Conv2D_BN_n3_Activation)
        n2_Backbone_n20_mixed_9_n5_Conv2D_BN_n2_BatchNormalization = layer_60a5c90c82ffc54caedc478d.BatchNormalization()(n2_Backbone_n20_mixed_9_n5_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n20_mixed_9_n5_Conv2D_BN_n3_Activation = layer_60a5c90c82ffc54caedc478f.Activation(activation='relu')(n2_Backbone_n20_mixed_9_n5_Conv2D_BN_n2_BatchNormalization)
        num_args = len(inspect.getfullargspec(layer_60a5c90c82ffc54caedc4792.Concatenate(axis=-1).call).args)
        if num_args == 2:
            n2_Backbone_n20_mixed_9_n6_Concatenate = layer_60a5c90c82ffc54caedc4792.Concatenate(axis=-1)([n2_Backbone_n20_mixed_9_n4_Conv2D_BN_n3_Activation, n2_Backbone_n20_mixed_9_n5_Conv2D_BN_n3_Activation])
        else:
            n2_Backbone_n20_mixed_9_n6_Concatenate = layer_60a5c90c82ffc54caedc4792.Concatenate(axis=-1)(*[n2_Backbone_n20_mixed_9_n4_Conv2D_BN_n3_Activation, n2_Backbone_n20_mixed_9_n5_Conv2D_BN_n3_Activation])
        n2_Backbone_n20_mixed_9_n7_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc4796.Conv2D(filters=448, kernel_size=[1, 1], strides=[1, 1], padding='valid', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n20_mixed_9_n2_Activation)
        n2_Backbone_n20_mixed_9_n7_Conv2D_BN_n2_BatchNormalization = layer_60a5c90c82ffc54caedc4798.BatchNormalization()(n2_Backbone_n20_mixed_9_n7_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n20_mixed_9_n7_Conv2D_BN_n3_Activation = layer_60a5c90c82ffc54caedc479a.Activation(activation='relu')(n2_Backbone_n20_mixed_9_n7_Conv2D_BN_n2_BatchNormalization)
        n2_Backbone_n20_mixed_9_n8_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc479e.Conv2D(filters=384, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n20_mixed_9_n7_Conv2D_BN_n3_Activation)
        n2_Backbone_n20_mixed_9_n8_Conv2D_BN_n2_BatchNormalization = layer_60a5c90c82ffc54caedc47a0.BatchNormalization()(n2_Backbone_n20_mixed_9_n8_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n20_mixed_9_n8_Conv2D_BN_n3_Activation = layer_60a5c90c82ffc54caedc47a2.Activation(activation='relu')(n2_Backbone_n20_mixed_9_n8_Conv2D_BN_n2_BatchNormalization)
        n2_Backbone_n20_mixed_9_n9_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc47a6.Conv2D(filters=384, kernel_size=[3, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n20_mixed_9_n8_Conv2D_BN_n3_Activation)
        n2_Backbone_n20_mixed_9_n9_Conv2D_BN_n2_BatchNormalization = layer_60a5c90c82ffc54caedc47a8.BatchNormalization()(n2_Backbone_n20_mixed_9_n9_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n20_mixed_9_n9_Conv2D_BN_n3_Activation = layer_60a5c90c82ffc54caedc47aa.Activation(activation='relu')(n2_Backbone_n20_mixed_9_n9_Conv2D_BN_n2_BatchNormalization)
        n2_Backbone_n20_mixed_9_n10_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc47ae.Conv2D(filters=384, kernel_size=[1, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n20_mixed_9_n8_Conv2D_BN_n3_Activation)
        n2_Backbone_n20_mixed_9_n10_Conv2D_BN_n2_BatchNormalization = layer_60a5c90c82ffc54caedc47b0.BatchNormalization()(n2_Backbone_n20_mixed_9_n10_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n20_mixed_9_n10_Conv2D_BN_n3_Activation = layer_60a5c90c82ffc54caedc47b2.Activation(activation='relu')(n2_Backbone_n20_mixed_9_n10_Conv2D_BN_n2_BatchNormalization)
        num_args = len(inspect.getfullargspec(layer_60a5c90c82ffc54caedc47b5.Concatenate(axis=-1).call).args)
        if num_args == 2:
            n2_Backbone_n20_mixed_9_n11_Concatenate = layer_60a5c90c82ffc54caedc47b5.Concatenate(axis=-1)([n2_Backbone_n20_mixed_9_n10_Conv2D_BN_n3_Activation, n2_Backbone_n20_mixed_9_n9_Conv2D_BN_n3_Activation])
        else:
            n2_Backbone_n20_mixed_9_n11_Concatenate = layer_60a5c90c82ffc54caedc47b5.Concatenate(axis=-1)(*[n2_Backbone_n20_mixed_9_n10_Conv2D_BN_n3_Activation, n2_Backbone_n20_mixed_9_n9_Conv2D_BN_n3_Activation])
        n2_Backbone_n20_mixed_9_n12_AveragePooling2D = layer_60a5c90c82ffc54caedc47b7.AveragePooling2D(pool_size=[3, 3], strides=[1, 1], padding='same')(n2_Backbone_n20_mixed_9_n2_Activation)
        n2_Backbone_n20_mixed_9_n13_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc47bb.Conv2D(filters=192, kernel_size=[1, 1], strides=[1, 1], padding='valid', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n20_mixed_9_n12_AveragePooling2D)
        n2_Backbone_n20_mixed_9_n13_Conv2D_BN_n2_BatchNormalization = layer_60a5c90c82ffc54caedc47bd.BatchNormalization()(n2_Backbone_n20_mixed_9_n13_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n20_mixed_9_n13_Conv2D_BN_n3_Activation = layer_60a5c90c82ffc54caedc47bf.Activation(activation='relu')(n2_Backbone_n20_mixed_9_n13_Conv2D_BN_n2_BatchNormalization)
        n2_Backbone_n20_mixed_9_n1_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc4771.Conv2D(filters=320, kernel_size=[1, 1], strides=[1, 1], padding='valid', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n20_mixed_9_n2_Activation)
        n2_Backbone_n20_mixed_9_n1_Conv2D_BN_n2_BatchNormalization = layer_60a5c90c82ffc54caedc4773.BatchNormalization()(n2_Backbone_n20_mixed_9_n1_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n20_mixed_9_n1_Conv2D_BN_n3_Activation = layer_60a5c90c82ffc54caedc4775.Activation(activation='relu')(n2_Backbone_n20_mixed_9_n1_Conv2D_BN_n2_BatchNormalization)
        num_args = len(inspect.getfullargspec(layer_60a5c90c82ffc54caedc47c4.Concatenate(axis=-1).call).args)
        if num_args == 2:
            n2_Backbone_n20_mixed_9_n14_Concatenate = layer_60a5c90c82ffc54caedc47c4.Concatenate(axis=-1)([n2_Backbone_n20_mixed_9_n6_Concatenate, n2_Backbone_n20_mixed_9_n11_Concatenate, n2_Backbone_n20_mixed_9_n1_Conv2D_BN_n3_Activation, n2_Backbone_n20_mixed_9_n13_Conv2D_BN_n3_Activation])
        else:
            n2_Backbone_n20_mixed_9_n14_Concatenate = layer_60a5c90c82ffc54caedc47c4.Concatenate(axis=-1)(*[n2_Backbone_n20_mixed_9_n6_Concatenate, n2_Backbone_n20_mixed_9_n11_Concatenate, n2_Backbone_n20_mixed_9_n1_Conv2D_BN_n3_Activation, n2_Backbone_n20_mixed_9_n13_Conv2D_BN_n3_Activation])
        n2_Backbone_n21_mixed_9_n2_Activation = layer_60a5c90c82ffc54caedc47d0.Activation(activation='linear')(n2_Backbone_n20_mixed_9_n14_Concatenate)
        n2_Backbone_n21_mixed_9_n3_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc47d4.Conv2D(filters=384, kernel_size=[1, 1], strides=[1, 1], padding='valid', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n21_mixed_9_n2_Activation)
        n2_Backbone_n21_mixed_9_n3_Conv2D_BN_n2_BatchNormalization = layer_60a5c90c82ffc54caedc47d6.BatchNormalization()(n2_Backbone_n21_mixed_9_n3_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n21_mixed_9_n3_Conv2D_BN_n3_Activation = layer_60a5c90c82ffc54caedc47d8.Activation(activation='relu')(n2_Backbone_n21_mixed_9_n3_Conv2D_BN_n2_BatchNormalization)
        n2_Backbone_n21_mixed_9_n4_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc47dc.Conv2D(filters=384, kernel_size=[1, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n21_mixed_9_n3_Conv2D_BN_n3_Activation)
        n2_Backbone_n21_mixed_9_n4_Conv2D_BN_n2_BatchNormalization = layer_60a5c90c82ffc54caedc47de.BatchNormalization()(n2_Backbone_n21_mixed_9_n4_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n21_mixed_9_n4_Conv2D_BN_n3_Activation = layer_60a5c90c82ffc54caedc47e0.Activation(activation='relu')(n2_Backbone_n21_mixed_9_n4_Conv2D_BN_n2_BatchNormalization)
        n2_Backbone_n21_mixed_9_n5_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc47e4.Conv2D(filters=384, kernel_size=[3, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n21_mixed_9_n3_Conv2D_BN_n3_Activation)
        n2_Backbone_n21_mixed_9_n5_Conv2D_BN_n2_BatchNormalization = layer_60a5c90c82ffc54caedc47e6.BatchNormalization()(n2_Backbone_n21_mixed_9_n5_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n21_mixed_9_n5_Conv2D_BN_n3_Activation = layer_60a5c90c82ffc54caedc47e8.Activation(activation='relu')(n2_Backbone_n21_mixed_9_n5_Conv2D_BN_n2_BatchNormalization)
        num_args = len(inspect.getfullargspec(layer_60a5c90c82ffc54caedc47eb.Concatenate(axis=-1).call).args)
        if num_args == 2:
            n2_Backbone_n21_mixed_9_n6_Concatenate = layer_60a5c90c82ffc54caedc47eb.Concatenate(axis=-1)([n2_Backbone_n21_mixed_9_n4_Conv2D_BN_n3_Activation, n2_Backbone_n21_mixed_9_n5_Conv2D_BN_n3_Activation])
        else:
            n2_Backbone_n21_mixed_9_n6_Concatenate = layer_60a5c90c82ffc54caedc47eb.Concatenate(axis=-1)(*[n2_Backbone_n21_mixed_9_n4_Conv2D_BN_n3_Activation, n2_Backbone_n21_mixed_9_n5_Conv2D_BN_n3_Activation])
        n2_Backbone_n21_mixed_9_n7_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc47ef.Conv2D(filters=448, kernel_size=[1, 1], strides=[1, 1], padding='valid', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n21_mixed_9_n2_Activation)
        n2_Backbone_n21_mixed_9_n7_Conv2D_BN_n2_BatchNormalization = layer_60a5c90c82ffc54caedc47f1.BatchNormalization()(n2_Backbone_n21_mixed_9_n7_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n21_mixed_9_n7_Conv2D_BN_n3_Activation = layer_60a5c90c82ffc54caedc47f3.Activation(activation='relu')(n2_Backbone_n21_mixed_9_n7_Conv2D_BN_n2_BatchNormalization)
        n2_Backbone_n21_mixed_9_n8_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc47f7.Conv2D(filters=384, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n21_mixed_9_n7_Conv2D_BN_n3_Activation)
        n2_Backbone_n21_mixed_9_n8_Conv2D_BN_n2_BatchNormalization = layer_60a5c90c82ffc54caedc47f9.BatchNormalization()(n2_Backbone_n21_mixed_9_n8_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n21_mixed_9_n8_Conv2D_BN_n3_Activation = layer_60a5c90c82ffc54caedc47fb.Activation(activation='relu')(n2_Backbone_n21_mixed_9_n8_Conv2D_BN_n2_BatchNormalization)
        n2_Backbone_n21_mixed_9_n9_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc47ff.Conv2D(filters=384, kernel_size=[3, 1], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n21_mixed_9_n8_Conv2D_BN_n3_Activation)
        n2_Backbone_n21_mixed_9_n9_Conv2D_BN_n2_BatchNormalization = layer_60a5c90c82ffc54caedc4801.BatchNormalization()(n2_Backbone_n21_mixed_9_n9_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n21_mixed_9_n9_Conv2D_BN_n3_Activation = layer_60a5c90c82ffc54caedc4803.Activation(activation='relu')(n2_Backbone_n21_mixed_9_n9_Conv2D_BN_n2_BatchNormalization)
        n2_Backbone_n21_mixed_9_n10_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc4807.Conv2D(filters=384, kernel_size=[1, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n21_mixed_9_n8_Conv2D_BN_n3_Activation)
        n2_Backbone_n21_mixed_9_n10_Conv2D_BN_n2_BatchNormalization = layer_60a5c90c82ffc54caedc4809.BatchNormalization()(n2_Backbone_n21_mixed_9_n10_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n21_mixed_9_n10_Conv2D_BN_n3_Activation = layer_60a5c90c82ffc54caedc480b.Activation(activation='relu')(n2_Backbone_n21_mixed_9_n10_Conv2D_BN_n2_BatchNormalization)
        num_args = len(inspect.getfullargspec(layer_60a5c90c82ffc54caedc480e.Concatenate(axis=-1).call).args)
        if num_args == 2:
            n2_Backbone_n21_mixed_9_n11_Concatenate = layer_60a5c90c82ffc54caedc480e.Concatenate(axis=-1)([n2_Backbone_n21_mixed_9_n10_Conv2D_BN_n3_Activation, n2_Backbone_n21_mixed_9_n9_Conv2D_BN_n3_Activation])
        else:
            n2_Backbone_n21_mixed_9_n11_Concatenate = layer_60a5c90c82ffc54caedc480e.Concatenate(axis=-1)(*[n2_Backbone_n21_mixed_9_n10_Conv2D_BN_n3_Activation, n2_Backbone_n21_mixed_9_n9_Conv2D_BN_n3_Activation])
        n2_Backbone_n21_mixed_9_n12_AveragePooling2D = layer_60a5c90c82ffc54caedc4810.AveragePooling2D(pool_size=[3, 3], strides=[1, 1], padding='same')(n2_Backbone_n21_mixed_9_n2_Activation)
        n2_Backbone_n21_mixed_9_n13_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc4814.Conv2D(filters=192, kernel_size=[1, 1], strides=[1, 1], padding='valid', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n21_mixed_9_n12_AveragePooling2D)
        n2_Backbone_n21_mixed_9_n13_Conv2D_BN_n2_BatchNormalization = layer_60a5c90c82ffc54caedc4816.BatchNormalization()(n2_Backbone_n21_mixed_9_n13_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n21_mixed_9_n13_Conv2D_BN_n3_Activation = layer_60a5c90c82ffc54caedc4818.Activation(activation='relu')(n2_Backbone_n21_mixed_9_n13_Conv2D_BN_n2_BatchNormalization)
        n2_Backbone_n21_mixed_9_n1_Conv2D_BN_n1_Conv2D = layer_60a5c90c82ffc54caedc47ca.Conv2D(filters=320, kernel_size=[1, 1], strides=[1, 1], padding='valid', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n21_mixed_9_n2_Activation)
        n2_Backbone_n21_mixed_9_n1_Conv2D_BN_n2_BatchNormalization = layer_60a5c90c82ffc54caedc47cc.BatchNormalization()(n2_Backbone_n21_mixed_9_n1_Conv2D_BN_n1_Conv2D)
        n2_Backbone_n21_mixed_9_n1_Conv2D_BN_n3_Activation = layer_60a5c90c82ffc54caedc47ce.Activation(activation='relu')(n2_Backbone_n21_mixed_9_n1_Conv2D_BN_n2_BatchNormalization)
        num_args = len(inspect.getfullargspec(layer_60a5c90c82ffc54caedc481d.Concatenate(axis=-1).call).args)
        if num_args == 2:
            n2_Backbone_n21_mixed_9_n14_Concatenate = layer_60a5c90c82ffc54caedc481d.Concatenate(axis=-1)([n2_Backbone_n21_mixed_9_n6_Concatenate, n2_Backbone_n21_mixed_9_n11_Concatenate, n2_Backbone_n21_mixed_9_n1_Conv2D_BN_n3_Activation, n2_Backbone_n21_mixed_9_n13_Conv2D_BN_n3_Activation])
        else:
            n2_Backbone_n21_mixed_9_n14_Concatenate = layer_60a5c90c82ffc54caedc481d.Concatenate(axis=-1)(*[n2_Backbone_n21_mixed_9_n6_Concatenate, n2_Backbone_n21_mixed_9_n11_Concatenate, n2_Backbone_n21_mixed_9_n1_Conv2D_BN_n3_Activation, n2_Backbone_n21_mixed_9_n13_Conv2D_BN_n3_Activation])
        n3_GlobalAveragePooling2D = layer_60a5c90c82ffc54caedc481f.GlobalAveragePooling2D()(n2_Backbone_n21_mixed_9_n14_Concatenate)
        n9_Dropout = layer_60a5c90c82ffc54caedc4823.Dropout(rate=0.5)(n3_GlobalAveragePooling2D)
        n4_Dense = layer_60a5c90c82ffc54caedc4821.Dense(units=6, activation='softmax', use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n9_Dropout)
        label = keras.layers.Input(shape=[6])
        loss = keras.losses.CategoricalCrossentropy()(label, n4_Dense)
        



        for key in list(config_loss.keys()):
            if len(config_loss[key]) == 1:
                config_loss[key] = config_loss[key][0]
            elif len(config_loss[key]) > 1:
                config_loss[key] = get_loss_sum_fn(config_loss[key])
            else:
                del config_loss[key]
        inputs = [n1_Image]
        outputs = [n4_Dense]
        losses = [loss]
        labels = [label]

        return inputs, outputs, losses, labels

