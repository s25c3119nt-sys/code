#ifndef PHILO_H
# define PHILO_H

# include <pthread.h>
# include <stdlib.h>
# include <stdio.h>
# include <unistd.h>
# include <sys/time.h>

typedef struct s_data	t_data;

typedef struct s_philo
{
	int				id;
	int				eat_count;
	long			last_meal;
	pthread_t		thread;
	pthread_mutex_t	*left;
	pthread_mutex_t	*right;
	t_data			*data;
}	t_philo;

typedef struct s_data
{
	int				num;
	int				time_die;
	int				time_eat;
	int				time_sleep;
	int				must_eat;
	int				stop;
	long			start;
	pthread_mutex_t	*forks;
	pthread_mutex_t	print;
	pthread_mutex_t	stop_mutex;
	pthread_mutex_t	meal_mutex;
	t_philo			*philos;
}	t_data;

/* utils */
long	ft_time(void);
int		ft_atoi(const char *s);

/* control */
int		get_stop(t_data *d);
void	set_stop(t_data *d, int val);

/* print */
void	ft_print(t_philo *p, char *msg);

/* thread */
void	*routine(void *arg);
void	*monitor(void *arg);

/* init */
void	init_data(t_data *d, int ac, char **av);
void	start_simulation(t_data *d);

/* free */
void	destroy_mutex(t_data *d);
void	free_all(t_data *d);

#endif