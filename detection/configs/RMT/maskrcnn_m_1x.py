_base_ = [
    '../_base_/models/RMT_rcnn.py',
    '../_base_/datasets/coco_instance.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]

model = dict(
    backbone=dict(
        embed_dims=[80, 160, 320, 512],
        depths=[4, 8, 25, 8],
        num_heads=[5, 5, 10, 16],
        init_values=[2, 2, 2, 2],
        heads_ranges=[5, 5, 6, 6],
        mlp_ratios=[4, 4, 3, 3],
        drop_path_rate=0.4,
        chunkwise_recurrents=[True, True, True, False],
        layerscales=[False, False, True, True],
        layer_init_values=1e-6,
        out_indices = (0, 1, 2, 3)
    ),
    neck = dict(in_channels=[80, 160, 320, 512])
)

optimizer = dict(_delete_=True, type='AdamW', lr=0.0004, betas=(0.9, 0.999), weight_decay=0.05,
                 paramwise_cfg=dict(custom_keys={'absolute_pos_embed': dict(decay_mult=0.),
                                                 'relative_position_bias_table': dict(decay_mult=0.),
                                                 'norm': dict(decay_mult=0.)}))
lr_config = dict(step=[8, 11])

# runner = dict(type='EpochBasedRunnerAmp', max_epochs=12)
# # do not use mmdet version fp16 -> WHY?
# fp16 = None
# optimizer_config = dict(
#     type="DistOptimizerHook",
#     update_interval=1,
#     grad_clip=None,
#     coalesce=True,
#     bucket_size_mb=-1,
#     use_fp16=True,
# )

fp16 = dict()
###########################################################################################################

# place holder for new verison mmdet compatiability
resume_from=None

# custom
checkpoint_config = dict(max_keep_ckpts=1)
runner = dict(work_dir='/mnt/bn/fqh-bytenas-data3/RMT_maskrcnn_m_1x')


data = dict(
    samples_per_gpu=4,
    workers_per_gpu=4,
)